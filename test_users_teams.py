import modrinth

# -----------------------------------

print("---- Get User Test: ----")

user = modrinth.get_user("WH9NfS5R")
print(user.display_name)

# -----------------------------------

print("---- Get Team Test: ----")

team = modrinth.get_team("BZoBsPo6")
for member in team.members:
    print(member.user.display_name)

# -----------------------------------