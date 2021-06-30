import modrinth

# ------------------------------------

search = modrinth.Search(
    categories=["fabric", "decoration"],
    sort="downloads",
    max_results=5
).search()

print("---- Search 1: ----")
for result in search.results:
    print(result.title)

# ------------------------------------

search = modrinth.Search(
    licenses=["mit"],
    max_results=8
).search()

print("---- Search 2: ----")
for result in search.results:
    print(result.title)

# ------------------------------------