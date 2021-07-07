import modrinth
import asyncio

async def async_main():
    modrinth.open()

    # -----------------------------------

    print("---- Search Test 1: ----")

    results = await modrinth.Search().search()
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

    modrinth.close()

loop = asyncio.get_event_loop() 
loop.run_until_complete(async_main())
