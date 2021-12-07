import click
from datetime import datetime
import asyncio

async def sleep_five():
    await asyncio.sleep(5)
    print("sleep five done")
    
async def sleep_three_then_five():
    await asyncio.sleep(3)
    await sleep_five()
    
async def main():
    await asyncio.gather(sleep_five(), sleep_three_then_five())
    
start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")