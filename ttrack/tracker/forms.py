from django import forms
from .models import Item, Kit, Request


class ItemForm(forms.ModelForm):
    # form to add additional items and show existing item details
    class Meta:
        model = Item
        exclude = ()
class KitForm(forms.ModelForm):
    # form to add additional items and show existing item details
    class Meta:
        model = Kit
        exclude = ()
class ReqForm(forms.ModelForm):
    # form to add additional items and show existing item details
    class Meta:
        model = Request
        exclude = ()
