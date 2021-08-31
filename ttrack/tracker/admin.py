from tracker.models import TRC, Borrower, Item, Item_Status, Kit, Location, Request
from django.contrib import admin

# Register your models here.
admin.site.register(Item)
admin.site.register(Request)
admin.site.register(TRC)
admin.site.register(Borrower)
admin.site.register(Location)
admin.site.register(Item_Status)
admin.site.register(Kit)

