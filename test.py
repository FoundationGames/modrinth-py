import modrinth

# ------------------------------------

results = modrinth.Search(
    categories=["fabric", "decoration"],
    sort="downloads",
    max_results=5
).search()

print("---- Search Test 1: ----")
for result in results.results:
    print(result.title)

# ------------------------------------

results = modrinth.Search(
    licenses=["mit"],
    max_results=8
).search()

print("---- Search Test 2: ----")
for result in results.results:
    print(result.title)

# ------------------------------------

user = modrinth.get_user("WH9NfS5R")
print("---- Get User Test: ----")
print(user.display_name)


# -----------------------------------

mod = modrinth.get_mod("5g7OOxWC")
print("---- Get Mod Test: ----")
print(mod.donation_urls)
print(type(mod.donation_urls))


