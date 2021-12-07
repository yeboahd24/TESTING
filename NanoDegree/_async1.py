import asyncio
from datetime import datetime
import click
import time

def sleep_and_print(seconds):
    print(f"starting {seconds} sleep")
    time.sleep(seconds)
    print(f"finished {seconds} sleep")
    return seconds

start = datetime.now()
print(sleep_and_print(3), sleep_and_print(6))
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
    
async def sleep_and_print(seconds):
    print(f"starting {seconds} sleep async")
    await asyncio.sleep(seconds)
    print(f"finished {seconds} sleep async")
    return seconds

async def main():
    results = await asyncio.gather(sleep_and_print(3), sleep_and_print(6))
    return results
    
start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")

