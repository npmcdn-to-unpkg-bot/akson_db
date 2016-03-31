from jqgrid import JqGrid
from django.core.urlresolvers import reverse_lazy

from models import NeurorehabilitationCard

class ExampleGrid(JqGrid):
    model = NeurorehabilitationCard # could also be a queryset
    fields = ['id', 'date', ] # optional 
    url = reverse_lazy('grid_handler')
    caption = 'My First Grid' # optional
    colmodel_overrides = {'id': { 'editable': False, 'width':20  },}
