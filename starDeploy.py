from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})

def startup():
	print("Holder Value")

routes = []

app = Starlette(debug=True, routes=routes, on_startup=[startup])
