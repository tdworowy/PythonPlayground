import asyncio


async def hello():
    print("HELLO")


async def print_number(number):
    print(number)


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())

    loop.run_until_complete(asyncio.wait([
        print_number(number) for number in range(10)
    ]))

    loop.close()
