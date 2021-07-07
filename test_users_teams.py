import modrinth
import asyncio

# -----------------------------------

"""print("---- Get User Test: ----")

user = modrinth.get_user("Gzv0LYLX")
print(user.display_name)"""

# -----------------------------------

"""print("---- Get Team Test: ----")

team = modrinth.get_team("Gzv0LYLX")
for member in team.members:
    print(member.user.display_name)"""

# -----------------------------------

mod2 = modrinth.get_mod("sandwichable")
print(mod2.versions)

"""print("mod async test")
async def main():
    mod = await modrinth.get_mod_async("sandwichable")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())"""