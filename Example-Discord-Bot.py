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
bot = commands.Bot("..", intents = intents)
bot.remove_command("help")



@bot.event
async def on_ready():
    print(f"Modrinth bot ready")

@bot.command()
async def search(ctx, search : str = None):

    results = modrinth.Search(
        query=search,
        categories=["fabric"],
        max_results=8
    ).search()

    
    embed = discord.Embed()
    mymods = ""
    number = 0
    for result in results.results:
        number += 1
        mymods += f"``{number}.`` {result.title}\n"

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
        modtitle = mod.title
        moddescription = mod.description
        modclient = mod.client_side
        modserver = mod.server_side
        mod_icon = mod.icon_url
        mod_discord = mod.discord_url
        mod_downloads = mod.downloads
        mod_teamid = mod.team

        if mod_teamid:
            team = modrinth.get_team(mod_teamid)

        team_developers = team.team_id
        developer_string = ""
        number = 0
        for i in team_developers:
            number += 1
            user = modrinth.get_user(i)
            developer_string += f"``Developer {number}:`` **{user.username}**\n"



        embed.title = f"{modtitle} - slug: {modslug}"
        embed.description = f"{moddescription}\n\n``Team ID.`` {mod_teamid}\n{developer_string}"
        #embed.description = f"{moddescription}\n\n``Developer:`` {user.username}"
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
    token = "ODYwMjI2NTAwNzg3OTYxODg2.YN4KXA.rT4RxWyH8XHqAlzfxM00TiywNSU"
    bot.run(token)