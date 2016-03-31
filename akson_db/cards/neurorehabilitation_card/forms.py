from neurorehabilitation_card.models import *

from django.forms import ModelForm

class NeurorehabilitationCardForm(ModelForm):
    class Meta:
        model = NeurorehabilitationCard
        fields = ['patient', 'leading_people', 'date', ]

