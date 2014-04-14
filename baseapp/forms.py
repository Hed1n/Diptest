__author__ = 'Хедин'
from django import forms

class filterform(forms.Form):
    manufacturer = forms.ChoiceField()
    opt_power = forms.ChoiceField()
    repl_time = forms.ChoiceField()
    m_o_w = forms.ChoiceField()
    colored = forms.ChoiceField(widget=forms.CheckboxInput)
    radius = forms.ChoiceField()
    opt_power_cil = forms.ChoiceField()
    axis = forms.ChoiceField()

class add_form_lins(forms.Form):
    opt_power = forms.ChoiceField()
    radius = forms.ChoiceField()