from tracker.models import Item
from django.shortcuts import render

# Create your views here.
def items(request):
    items = Item.objects.all()
    
    context = {'items':items}
    return render(request, 'tracker/items.html', context)