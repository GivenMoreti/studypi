from django.db import models

# Create your models here.
CONDITIONS= (
  ("Good","Good"),
  ("Better","Better"),
  ("Best,","Best"),
)


class Item(models.Model):
  item_name = models.CharField(max_length=300,default=None)
  condition = models.CharField(max_length=300,default=None,choices=CONDITIONS)
  price =models.FloatField()
  summary = models.TextField()
  item_url = models.CharField(max_length=8000,null=True)
  date_added = models.DateField(auto_now_add=True,null=True)
  date_edited = models.DateField(auto_now=True,null=True)
    
 