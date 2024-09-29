from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#register it in admin
class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        ordering=('name',)
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name    
    
class Item(models.Model):
    category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE) 
    name=models.CharField(max_length=255)
    description=models.TextField(max_length=255,null=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='item_images',blank=True,null=True) #pip instal pillow
    is_sold=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name="items",on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Items'
        ordering=('name',)
    
    def __str__(self):
        return self.name