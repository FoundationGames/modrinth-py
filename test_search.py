import modrinth

# -----------------------------------

print("---- Search Test 1: ----")

results = modrinth.Search().search()
for result in results.results:
    print(result.title)

# -----------------------------------

print("---- Search Test 2: ----")

results = modrinth.Search(
    categories=["fabric", "decoration"],
    sort="downloads",
    max_results=5
).search()
for result in results.results:
    print(result.title)

# ------------------------------------

print("---- Search Test 3: ----")

results = modrinth.Search(
    licenses=["mit"],
    max_results=8
).search()
for result in results.results:
    print(result.title)

# ------------------------------------