from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE,related_name="todolist", null=True)
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Items(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self):
        return self.text