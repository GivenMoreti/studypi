from django.shortcuts import render
from .models import Item
from django.http import Http404
# Create your views here.


def item(request):
  try:
    items = Item.objects.all()
  except Item.DoesNotExist:
    raise Http404('item does not exist currently')
  return render (request,'items/items.html',{'items':items})