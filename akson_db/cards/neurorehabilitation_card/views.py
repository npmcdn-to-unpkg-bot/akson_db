from grids import ExampleGrid
from django.http import HttpResponse

def grid_handler(request):
    grid = ExampleGrid()
    return HttpResponse(grid.get_json(request), mimetype="application/json")

def grid_config(request):
    grid = ExampleGrid()
    return HttpResponse(grid.get_config(), mimetype="application/json")
