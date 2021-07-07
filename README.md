# modrinth.py
A (WORK IN PROGRESS) Modrinth API wrapper in Python


Quick Start
```python
import modrinth
import asyncio

async def main():

    # --- Search a mod by name ---

    print("--- Test 1 ---")

    async def search_function(query, amt):
        results = await modrinth.Search(
            query=query,
            max_results=amt,
        ).search()
        return results

    results = await search_function("dirty dirty sausage", 10)

    for result in results.results:
        print(result.title)
        print(result.id)

    # --- Get mod Information ---

    print("--- Test 2 ---")
    
    mod_id = "sandwichable" #it can also take slugs
    mod = await modrinth.get_mod(mod_id)
    print(mod.title)
    
    # ---------------------------
    
    await modrinth.close() #closes your session
  
loop = asyncio.get_event_loop() 
loop.run_until_complete(main())
  ```
  
