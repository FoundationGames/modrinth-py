import modrinth

# ------------------------------------

print("---- Get Mod Test: ----")

mod = modrinth.get_mod("AANobbMI")
for version in mod.versions:
    print(version.number)
for link in mod.donation_links:
    print(link.id+" "+link.url)

# -----------------------------------

print("---- Get Version Test: ----")

version = modrinth.get_version("W3lvWTIF")
print(version.number)
for file in version.files:
    print(file.filename)
    print(file.sha512)

# ------------------------------------