# modrinth.py
A (WORK IN PROGRESS) Modrinth API wrapper in Python


Quick Start
```python
async def main():

  # --- Search a mod by name ---
  
  async def search_function(query, amt):
      results = await modrinth.Search(
          query=query,
          max_results=amt,
      ).search()
      return results
  results = ("query", 10)
  
  # --- Get mod Information ---
  
  mod_id = "YOUR MOD ID"
  mod = await modrinth.get_mod(mod_id)
  print(mod.title)
  
  # ---------------------------
  
  await modrinth.close() #closes your session
  
loop = asyncio.get_event_loop() 
loop.run_until_complete(async_main())
  ```
  
