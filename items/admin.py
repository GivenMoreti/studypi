from django.contrib import admin

# Register your models here.
from .models import Item
class ItemAdmin(admin.ModelAdmin):
  list_display=('item_name','condition','price','summary','date_added','date_edited')

admin.site.register(Item,ItemAdmin)