import asyncio
import time


async def one(name):
    await asyncio.sleep(2)
    print(f"hi {name}")


print("#" * 5, s := "return async def", "#" * (70 - len(s)))
print(one("sajjad"))
print(type(one("sajjad")))

print("#" * 5, s := "use asuncio.run", "#" * (70 - len(s)))
start = time.perf_counter()
asyncio.run(one("sajjad"))
asyncio.run(one("webneshin"))
end = time.perf_counter()
print("*" * 10, end - start, "*" * 10)

print("#" * 5, s := "use create_task", "#" * (70 - len(s)))


async def main():
    a = asyncio.create_task(one("sajjad"))
    b = asyncio.create_task(one("webneshin"))

    await a
    await b


start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()
print("*" * 10, end - start, "*" * 10)