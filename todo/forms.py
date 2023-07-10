from django import forms
from todo.models import Item

DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')


class ItemForm(forms.ModelForm):
    due_date = forms.DateField(
        label="Vencimento", required=True, input_formats=DATE_INPUT_FORMATS,
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}),)

    class Meta:
        model = Item
        fields = ['description', 'due_date', 'checked',]
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
