import modrinth
import asyncio

# ------------------------------------

async def main():
    async with modrinth.ModrinthSession() as session:
        # ------------------------------------

        print("---- Get Mod Test: ----")

        mod = await session.get_mod("5g7OOxWC")
        versions = await mod.get_versions()

        for version in versions:
            print(version.name)

        print(version.date_published)

        # -----------------------------------

        print("---- Get Version Test: ----")

        version = await session.get_version("W3lvWTIF")
        print(version.number)
        for file in version.files:
            print(file.filename)
            print(file.sha512)

        # ------------------------------------



loop = asyncio.get_event_loop()
loop.run_until_complete(main())