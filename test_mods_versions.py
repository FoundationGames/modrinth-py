import modrinth
import asyncio

# ------------------------------------

async def main():

    # ------------------------------------

    print("---- Get Mod Test: ----")

    mod = await modrinth.get_mod("5g7OOxWC")
    versions = await mod.get_versions()

    for version in versions:
        print(version.name)
        print(version.changelog)

    # -----------------------------------

    print("---- Get Version Test: ----")

    version = await modrinth.get_version("W3lvWTIF")
    print(version.number)
    for file in version.files:
        print(file.filename)
        print(file.sha512)

    # ------------------------------------

    await modrinth.close()



loop = asyncio.get_event_loop() 
loop.run_until_complete(main())