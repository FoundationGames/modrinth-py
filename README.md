# modrinth.py
A (WORK IN PROGRESS) Modrinth API wrapper in Python


Quick Start
```python
import modrinth
import asyncio

async def main():
    async with modrinth.ModrinthSession() as session:
        # --- Search a mod by name ---

        print("--- Test 1 ---")

        async def search_function(query, amt):
            results = await session.search(
                modrinth.Search(
                    query=query,
                    max_results=amt,
                )
            )
            return results

        results = await search_function("dirty dirty sausage", 10)

        for result in results.results:
            print(result.title)
            print(result.id)

        # --- Get mod Information ---

        print("--- Test 2 ---")

        mod_id = "sandwichable" #it can also take slugs
        mod = await session.get_mod(mod_id)
        print(mod.title)

        # ---------------------------



loop = asyncio.get_event_loop() 
loop.run_until_complete(main())
      ```
  
