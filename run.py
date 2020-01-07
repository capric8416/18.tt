# -*- coding: utf-8 -*-


from aiohttp import web


static = '/home/pi/18.tt/static'
static_html = f'{static}/html'
static_apps = f'{static}/apps'
html_type = {'Content-Type': 'text/html'}


async def index(request):
    with open(f'{static_html}/index.html') as fp:
        return web.Response(text=fp.read().replace('$my_ip$', request.headers.get('X-Real-IP') or request.remote), headers=html_type)


async def tool(request):
    with open(f'{static_html}/{request.match_info["name"]}.html') as fp:
        return web.Response(text=fp.read(), headers=html_type)


async def play(request):
    with open(f'{static_html}/{request.match_info["mode"]}.html') as fp:
        return web.Response(text=fp.read().replace('$video_name$', request.match_info['name']), headers=html_type)


async def ip(request):
    return web.json_response({'ip': request.headers.get('X-Real-IP') or request.remote})



if __name__ == '__main__':
    app = web.Application()

    app.add_routes([
        web.get('/', index),
        web.get('/query/ip', ip),
        web.get('/tool/{name:.+}', tool),
        web.get('/play/{mode:.+?}/{name:.+}', play),
        web.static('/static', static, show_index=False, follow_symlinks=False),
        web.static('/apps', static_apps, show_index=True, follow_symlinks=True),
    ])

    web.run_app(app, host='0.0.0.0', port=80)

