import discord
import random
import shutil
import json
import asyncio
from discord import Embed 
from discord.ext import commands

# ---------
import modrinth
# -------- 

# This is an Example of what you can make with Modrinth.py 
# Feel free to use any code in this file.

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot("m!", intents = intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f"Modrinth bot ready")

@bot.command()
@commands.max_concurrency(1,per=commands.BucketType.user,wait=False)
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
    if not mymods:
        embed.description = "No mods were found."
        await ogmessage.edit(embed=embed)
        return
    await ogmessage.edit(embed=embed)
    async def add_multiple_reactions(message, reactions, number): 
        amount_ = 0
        for r in range(number):
            await message.add_reaction(reactions[amount_])
            amount_ += 1

            
    my_reaction = ('1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟','🚫')
    asyncio.create_task(add_multiple_reactions(ogmessage, my_reaction, number))
    jump_url = ogmessage.jump_url
    def check(reaction, user):
        return user == ctx.author
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:

        return
    else:
        reaction = str(reaction)
        if reaction == '1️⃣':
            await find_mod(ctx, id_result[0], jump_url)
            await ogmessage.clear_reactions()
        elif reaction == '2️⃣':
            await find_mod(ctx, id_result[1], jump_url)
            await ogmessage.clear_reactions()
        elif reaction == '3️⃣':
            await find_mod(ctx, id_result[2], jump_url)
            await ogmessage.clear_reactions()
        elif reaction == '4️⃣':
            await find_mod(ctx, id_result[3], jump_url)
            await ogmessage.clear_reactions()
        elif reaction == '5️⃣':
            await find_mod(ctx, id_result[4], jump_url)
            await ogmessage.clear_reactions()
        elif reaction == '6️⃣':
            await find_mod(ctx, id_result[5], jump_url)
            await ogmessage.clear_reactions()
        elif reaction == '7️⃣':
            await find_mod(ctx, id_result[6], jump_url)
            await ogmessage.clear_reactions()
        elif reaction == '8️⃣':
            await find_mod(ctx, id_result[7], jump_url)
            await ogmessage.clear_reactions()
        elif reaction == '9️⃣':
            await find_mod(ctx, id_result[8], jump_url)
            await ogmessage.clear_reactions()
        elif reaction == '🔟':
            await find_mod(ctx, id_result[9], jump_url)
            await ogmessage.clear_reactions()
        else:
            await ogmessage.clear_reactions()
            return


@bot.command()
async def user(ctx, user_id : str = None):
    if user_id == None:
        await ctx.send("You need to specify a ``user id``.")
        return
    
    user = await modrinth.get_user(user_id)


    embed = discord.Embed()
    embed.title = f"{user.display_name}'s profile"
    embed.description = f"{user.bio}\n\nUser ID: ``{user.id}``"
    #embed.add_field(name = "Email", value = user.email) for some reason email always sends None
    #embed.add_field(name = "Created", value = user.created) 
    embed.add_field(name = "Role", value = user.role)
    embed.add_field(name = "Github id", value = user.github_id)
    embed.set_thumbnail(url = user.avatar_url)

    await ctx.send(embed=embed)


@bot.command()
async def version(ctx, version_id : str = None):
    if version_id == None:
        await ctx.send("You need to specify a ``user id``.")
        return
    
    user = await modrinth.get_version(version_id)


    embed = discord.Embed()
    embed.title = f"{user.display_name}'s profile"
    embed.description = f"{user.bio}\n\nUser ID: ``{user.id}``"
    #embed.add_field(name = "Email", value = user.email) for some reason email always sends None
    #embed.add_field(name = "Created", value = user.created) 
    embed.add_field(name = "Role", value = user.role)
    embed.add_field(name = "Github id", value = user.github_id)
    embed.set_thumbnail(url = user.avatar_url)

    await ctx.send(embed=embed)

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
        mod_issues = mod.issues_url
        mod_downloads = mod.downloads
        mod_categories = mod.categories
        mod_published = mod.published
        mod_updated = mod.updated
        categories_list = ""
        for categories in mod_categories:
            categories_list += (f"{categories}, ")
        team = await modrinth.get_team(mod.team_id)
        developer_string = ""
        number = 0
        for member in team.team_info:
            user = await modrinth.get_user(member["user_id"])
            number += 1
            role = member["role"]
            developer_string += f"``Developer {number}:`` **[{user.display_name}](https://modrinth.com/user/{user.id})** - **{role}**\n"

        embed.title = f"{modtitle} - slug: {modslug}"
        embed.description = f"{moddescription}\n\n``Team ID.`` {mod.team_id}\n{developer_string}\n**__[VIEW MOD PAGE >](https://modrinth.com/mod/{mod_id})__**"
        embed.add_field(name = "Client Side", value = modclient)
        embed.add_field(name = "Server Side", value = modserver)
        embed.add_field(name = "Downloads", value = mod_downloads)
        embed.add_field(name = "Categories", value = categories_list)
        embed.add_field(name = "Published", value = mod_published)
        embed.add_field(name = "Updated", value = mod_updated)
        embed.add_field(name = "Issues", value = f"[Issues URL]({mod_issues})")
        embed.add_field(name = "Discord", value = f"[Support Server]({mod_discord})")
        try:
            embed.set_thumbnail(url = mod_icon)
        except:
            pass
        
        if editable:
            link = editable
            server_id = int(link[29:47])
            channel_id = int(link[48:66])
            msg_id = int(link[67:])
            server = bot.get_guild(server_id)
            channel = server.get_channel(channel_id)
            message = await channel.fetch_message(msg_id)
            return await message.edit(embed=embed)
        else:
            return await ctx.send(embed=embed)




    except Exception as e:
        print(e)
        return await ctx.send("There was an error")

async def search_function(query, amt):
    results = await modrinth.Search(
        query=query,
        max_results=amt,
    ).search()
    return results

@bot.command()
@commands.is_owner()
async def shutdown_bot(ctx):
    await modrinth.close() # Closes the session when the bot shuts down
    await ctx.send("shutting down.")
    exit()

@bot.command()
async def help(ctx):
    embed = discord.Embed()
    embed.title = "Help"
    embed.description = "This bot is a 'proof of concept' on what you can do with modrinth.py.\nCheck out the [API wrapper here](https://github.com/FoundationGames/modrinth-py)\nIf you have any questions join the [help server](https://discord.gg/sDrqXQ5XMy)"
    embed.add_field(name="Search for a Mod",value = "m!search ``<query>``")
    embed.add_field(name="Mod Info",value = "m!mod ``<mod slug/id>``")
    embed.add_field(name="User Info",value = "m!user ``<mod id>``")
    await ctx.send(embed=embed)
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.MaxConcurrencyReached):
        await ctx.author.send('This command can only be used once per session.')
        return

if __name__ == "__main__":
    token = ""
    # Make a json file in the root dir called "bot_config.json" with a single field called "bot_token"
    with open(file="bot_config.json") as f:
        token = json.load(f)["bot_token"]
    bot.run(token)
