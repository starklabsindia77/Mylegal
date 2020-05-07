from django.db import models


class Category(models.Model):
  categoryName  = models.CharField(max_length=60)
  status        = models.BooleanField(default=True) 
  created_at    = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return "%s"%(self.categoryName)

class IPC(models.Model):
  IPC_NUMBER = models.CharField(max_length=60)
  DESCRIPTION = models.TextField()
  CATEGORY_ID = models.ForeignKey(Category, on_delete=models.CASCADE)
  IMAGE = models.FileField(upload_to='uploads/', null = True, blank = True)
  STATUS = models.BooleanField(default=True) 
  CREATED_AT = models.DateTimeField(auto_now_add=True)


  class Meta:
    unique_together=('IPC_NUMBER',)

  def __str__(self):
    return "%s" %(self.IPC_NUMBER)
  