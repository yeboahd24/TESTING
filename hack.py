from aiohttp import web


with open('/home/dominic/TESTING/alpine/index.html', 'r') as f:
    code = f.read()

async def hello(request):
    return web.Response(text=code, content_type='text/html', charset='utf-8')

app = web.Application()
app.add_routes([web.get('/', hello)])

web.run_app(app)
