import discord
import random
import shutil
import json
import asyncio
import functools
from discord import Embed 
from discord.ext import commands

# ---------
import modrinth
# -------- 


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot("m!", intents = intents)
bot.remove_command("help")



@bot.event
async def on_ready():
    print(f"Modrinth bot ready")

@bot.command()
async def search(ctx, *, search : str = None):
    embed = discord.Embed()
    embed.title = "Searching..."
    embed.description = "Loading data"
    ogmessage = await ctx.send(embed=embed)
    results = await search_function(search, 10)
    embed = discord.Embed()
    mymods = ""
    number = 0
    id_result = []
    for result in results.results:
        number += 1
        mymods += f"``{number}.`` [{result.title}](https://modrinth.com/mod/{result.id})\n   **Mod ID:** {result.id}\n"
        id_result.append(result.id)

    embed.title = "List of Mods"
    embed.description = mymods
    embed.set_thumbnail(url = "https://cdn.discordapp.com/emojis/844330470719356970.png?v=1")
    await ogmessage.edit(embed=embed)
    async def add_multiple_reactions(message, reactions, number): #better because it's async
        amount_ = 0
        for r in range(number):
            await message.add_reaction(reactions[amount_])
            amount_ += 1

            
    my_reaction = ('1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟','🚫')
    asyncio.create_task(add_multiple_reactions(ogmessage, my_reaction, number))

    def check(reaction, user):
        return user == ctx.author
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:

        return
    else:
        reaction = str(reaction)
        if reaction == '1️⃣':
            await find_mod(ctx, id_result[0], ogmessage)
            await ogmessage.clear_reactions()
        elif reaction == '2️⃣':
            await find_mod(ctx, id_result[1], ogmessage)
            await ogmessage.clear_reactions()
        elif reaction == '3️⃣':
            await find_mod(ctx, id_result[2], ogmessage)
            await ogmessage.clear_reactions()
        elif reaction == '4️⃣':
            await find_mod(ctx, id_result[3], ogmessage)
            await ogmessage.clear_reactions()
        elif reaction == '5️⃣':
            await find_mod(ctx, id_result[4], ogmessage)
            await ogmessage.clear_reactions()
        elif reaction == '6️⃣':
            await find_mod(ctx, id_result[5], ogmessage)
            await ogmessage.clear_reactions()
        elif reaction == '7️⃣':
            await find_mod(ctx, id_result[6], ogmessage)
            await ogmessage.clear_reactions()
        elif reaction == '8️⃣':
            await find_mod(ctx, id_result[7], ogmessage)
            await ogmessage.clear_reactions()
        elif reaction == '9️⃣':
            await find_mod(ctx, id_result[8], ogmessage)
            await ogmessage.clear_reactions()
        elif reaction == '🔟':
            await find_mod(ctx, id_result[9], ogmessage)
            await ogmessage.clear_reactions()
        else:
            await ogmessage.clear_reactions()
            return

    


@bot.command()
async def mod(ctx, mod_id : str = None):
    await find_mod(ctx, mod_id)

async def find_mod(ctx, mod_id : str = None, editable = None):
    if mod_id == None:
        return await ctx.send("Specify a mod ID")

    try:
        mod = await modrinth.get_mod(mod_id)
        embed = discord.Embed()

        modslug = mod.slug
        mod_id = mod.id
        modtitle = mod.title
        moddescription = mod.description
        modclient = mod.client_side
        modserver = mod.server_side
        mod_icon = mod.icon_url
        mod_discord = mod.discord_url
        mod_downloads = mod.downloads
        mod_team = mod.team
        mod_team_id = mod.team_id

        developer_string = ""
        number = 0
        for member in mod_team.members:
            number += 1
            developer_string += f"``Developer {number}:`` **[{member.user.username}](https://modrinth.com/user/{member.user.id})**\n"

        embed.title = f"{modtitle} - slug: {modslug}"
        embed.description = f"{moddescription}\n\n``Team ID.`` {mod_team_id}\n{developer_string}\n**__[VIEW MOD PAGE >](https://modrinth.com/mod/{mod_id})__**"
        embed.add_field(name = "Client Side", value = modclient)
        embed.add_field(name = "Server Side", value = modserver)
        embed.add_field(name = "Downloads", value = mod_downloads)
        embed.add_field(name = "Issues", value = f"[Issues URL]({mod_discord})")
        embed.add_field(name = "Discord", value = f"[Support Server]({mod_discord})")
        embed.set_thumbnail(url = mod_icon)
        
        if editable:
            return await editable.edit(embed=embed)
        else:
            return await ctx.send(embed=embed)




    except Exception as e:
        print(e)
        return await ctx.send("There was an error")

async def search_function(query, amt):
    print(query)
    results = await modrinth.Search(
        query=query,
        max_results=amt,
    ).search()
    return results



if __name__ == "__main__":
    token = ""
    # Make a json file in the root dir called "bot_config.json" with a single field called "bot_token"
    with open(file="bot_config.json") as f:
        token = json.load(f)["bot_token"]
    bot.run(token)
