import asyncio
import aiofiles
import os
import aiohttp
import time
async def download_html(session,url):
    async with session.get(url,ssl=False) as res:
        filename=f"output/{os.path.basename(url)}.html"
        async with aiofiles.open(filename,"wb") as f:
            while True:
                #with await ,event loop switch to another task,and again switch to another task at await in the task
                chunk = await res.content.read(1024)
                if not chunk:
                    break
                await f.write(chunk)
        return  await res.release()


async def main(url):
    async with aiohttp.ClientSession() as session:
        await download_html(session,url)

urls=[
    "http://packtpub.com",
    "http://python.org",
    "http://google.com"
]

st=time.perf_counter()

loop=asyncio.get_event_loop()
loop.run_until_complete(
asyncio.gather(*(main(url) for url in urls))
)
print(time.perf_counter()-stlmkd)