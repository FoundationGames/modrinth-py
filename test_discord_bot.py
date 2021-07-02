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


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot("m!", intents = intents)
bot.remove_command("help")



@bot.event
async def on_ready():
    print(f"Modrinth bot ready")

@bot.command()
async def search(ctx, search : str = None):

    results = modrinth.Search(
        query=search,
        max_results=10
    ).search()

    
    embed = discord.Embed()
    mymods = ""
    number = 0
    for result in results.results:
        number += 1
        mymods += f"``{number}.`` {result.title} **ID:** ````\n"

    embed.title = "List of Mods"
    embed.description = mymods
    
    await ctx.send(embed=embed)

@bot.command()
async def mod(ctx, mod_id : str = None):
    if mod_id == None:
        return await ctx.send("Specify a mod ID")

    try:
        mod = modrinth.get_mod(mod_id)
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
            developer_string += f"``Developer {number}:`` **{member.user.username}**\n"

        embed.title = f"{modtitle} - slug: {modslug}"
        embed.description = f"{moddescription}\n\n``Team ID.`` {mod_team_id}\n{developer_string}\n**__[VIEW MOD PAGE >](https://modrinth.com/mod/{mod_id})__**"
        embed.add_field(name = "Client Side", value = modclient)
        embed.add_field(name = "Server Side", value = modserver)
        embed.add_field(name = "Downloads", value = mod_downloads)
        embed.add_field(name = "Issues", value = f"[Issues URL]({mod_discord})")
        embed.add_field(name = "Discord", value = f"[Support Server]({mod_discord})")
        embed.set_thumbnail(url = mod_icon)

        await ctx.send(embed=embed)




    except Exception as e:
        print(e)
        return await ctx.send("There was an error")

    

if __name__ == "__main__":
    token = ""
    # Make a json file in the root dir called "bot_config.json" with a single field called "bot_token"
    with open(file="bot_config.json") as f:
        token = json.load(f)["bot_token"]
    bot.run(token)
