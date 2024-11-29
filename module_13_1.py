import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        time_ = 6 / (power/5)
        await asyncio.sleep(time_)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Mike', 5))
    task2 = asyncio.create_task(start_strongman('John', 15))
    task3 = asyncio.create_task(start_strongman('Jack', 10))
    await task1
    await task2
    await task3
asyncio.run(start_tournament())
