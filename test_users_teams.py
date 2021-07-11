import modrinth
import asyncio


async def main():
    async with modrinth.ModrinthSession() as session:
        # -----------------------------------

        print("---- Get User Test: ----")

        user = await session.get_user("TcDPJAHF")
        print(user.display_name)

        # -----------------------------------

        print("---- Get Team Test A: ----")

        mod = await session.get_mod("mOgUt4GM")
        mod_team_id = mod.team_id
        team = await session.get_team(mod_team_id)

        print(mod.title)
        print(team.user_ids)

        for member in team.user_ids:
            user = await session.get_user(member)
            print(user.display_name)

        # -----------------------------------

        print("---- Get Team Test B: ----")

        mod = await session.get_mod("mOgUt4GM")
        team = await mod.get_team()

        print(mod.title)
        print(team.user_ids)
        
        for member in team.user_ids:
            user = await session.get_user(member)
            print(f"{user.display_name} - {user.id}")


        # -----------------------------------

        print("---- Get Team Info: ----")

        mod = await session.get_mod("mOgUt4GM")
        team = await mod.get_team()

        for member in team.members:
            user_id = member.user_id
            user_role = member.role
            print(f"User ID: {user_id} - User Role: {user_role}")

    # Different ways of getting Info

    for member_info in team.team_info:
        user_id = member_info["user_id"]
        user_role = member_info["role"]
        print(f"User ID: {user_id} - User Role: {user_role}")

    print("--- Or ---")

    for member_info in team.members:
        user_id = member_info.user_id
        user_role = member_info.role
        print(f"User ID: {user_id} - User Role: {user_role}")



loop = asyncio.get_event_loop() 
loop.run_until_complete(main())