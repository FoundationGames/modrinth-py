import modrinth

# -----------------------------------

print("---- Get User Test: ----")

user = modrinth.get_user("Gzv0LYLX")
print(user.display_name)

# -----------------------------------

print("---- Get Team Test: ----")

team = modrinth.get_team("Gzv0LYLX")
for member in team.members:
    print(member.user.display_name)

# -----------------------------------