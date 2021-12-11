import asyncio
import random

old_list = [i for i in range(0, 10)]
new_list = []

async def picker():
    print(old_list, new_list)
    new_list.append(old_list.pop(random.randrange(len(old_list))))
    print(old_list, new_list)

async def main():
    tasks = []
    for _ in range(len(old_list)):
        tasks.append(asyncio.ensure_future(picker()))

    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()