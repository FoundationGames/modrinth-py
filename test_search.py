import modrinth
import asyncio

async def main():
    async with modrinth.ModrinthSession() as session:
        # -----------------------------------

        print("---- Search Test 1: ----")

        results = await session.search(
            modrinth.Search(query="sandwich")
        )
        for result in results.results:
            print(result.title)

        # -----------------------------------

        print("---- Search Test 2: ----")

        results = await session.search(
            modrinth.Search(
                categories=["fabric", "decoration"],
                sort="downloads",
                max_results=5
            )
        )
        for result in results.results:
            print(result.title)

        # ------------------------------------

        print("---- Search Test 3: ----")

        results = await session.search(
            modrinth.Search(
                licenses=["mit"],
                max_results=8
            )
        )
        for result in results.results:
            print(result.title)

        # ------------------------------------

loop = asyncio.get_event_loop() 
loop.run_until_complete(main())
