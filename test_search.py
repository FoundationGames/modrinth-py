import modrinth
import asyncio

async def async_main():

    # -----------------------------------

    print("---- Search Test 1: ----")

    results = await modrinth.Search(query="sandwich",).search()
    for result in results.results:
        print(result.title)

    # -----------------------------------

    print("---- Search Test 2: ----")

    results = await modrinth.Search(
        categories=["fabric", "decoration"],
        sort="downloads",
        max_results=5
    ).search()
    for result in results.results:
        print(result.title)

    # ------------------------------------

    print("---- Search Test 3: ----")

    results = await modrinth.Search(
        licenses=["mit"],
        max_results=8
    ).search()
    for result in results.results:
        print(result.title)

    # ------------------------------------

    print("---- Search Test 4: ----")
    mod = await modrinth.get_mod("mOgUt4GM")
    mod_team_id = mod.team_id
    team = await modrinth.get_team(mod_team_id)

    print(team.user_id)
    for member in team.user_id:
        user = await modrinth.get_user(member)
        print(user.display_name)
    # ------------------------------------
    await modrinth.close()

loop = asyncio.get_event_loop() 
loop.run_until_complete(async_main())
