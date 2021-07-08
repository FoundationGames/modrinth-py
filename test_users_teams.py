import modrinth
import asyncio


async def main():
    print("---- Get User Test: ----")

    user = await modrinth.get_user("TcDPJAHF")
    print(user.display_name)

    # -----------------------------------

    print("---- Get Team Test A: ----")

    mod = await modrinth.get_mod("mOgUt4GM")
    mod_team_id = mod.team_id
    team = await modrinth.get_team(mod_team_id)

    print(mod.title)
    print(team.user_id)

    for member in team.user_id:
        user = await modrinth.get_user(member)
        print(user.display_name)

    # -----------------------------------

    print("---- Get Team Test B: ----")

    mod = await modrinth.get_mod("mOgUt4GM")
    team = await mod.get_team()

    print(mod.title)
    print(team.user_id)
    
    for member in team.user_id:
        user = await modrinth.get_user(member)
        print(user.display_name)

    await modrinth.close() # Remember to Close all sessions at the end of the program. 

loop = asyncio.get_event_loop() 
loop.run_until_complete(main())