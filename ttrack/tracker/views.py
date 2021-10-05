from tracker.models import Item, Kit, Request
from django.shortcuts import render, redirect
from django.views import generic
from .forms import ItemForm, KitForm, ReqForm

# Create your views here.
def items(request):
    items = Item.objects.all()
    
    context = {'items':items}
    return render(request, 'tracker/items.html', context)

class ItemDetailView(generic.DetailView):
    model = Item


def new_item(request):
    #form to add new items to inventory
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = ItemForm()
    return render(request, 'tracker/new_item.html',
    {
        'form':form
    })
def item_edit(request, pk):
    item = Item.objects.get(pk = pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = ItemForm(instance=item)

    return render(request,
        'tracker/item_edit.html',
        {
            'form': form,
            'item': item
        })
def new_kit(request):
    #form to add new items to inventory
    if request.method == 'POST':
        form = KitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kit-list')
    else:
        form = KitForm()
    return render(request, 'tracker/new_kit.html',
    {
        'form':form
    })
class KitListView(generic.ListView):
    model = Kit
class KitDetailView(generic.DetailView):
    model = Kit
class ReqListView(generic.ListView):
    model = Request

def kit_edit(request, pk):
    kit = Kit.objects.get(pk = pk)
    if request.method == "POST":
        form = KitForm(request.POST, instance=kit)
        if form.is_valid():
            form.save()
            return redirect('kit-list')
    else:
        form = KitForm(instance=kit)

    return render(request,
        'tracker/kit_edit.html',
        {
            'form': form,
            'kit': kit
        })
def req_edit(request, pk):
    req = Request.objects.get(pk = pk)
    if request.method == "POST":
        form = ReqForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
            return redirect('req-list')
    else:
        form = ReqForm(instance=req)

    return render(request,
        'tracker/req_edit.html',
        {
            'form': form,
            'req': req
        })
