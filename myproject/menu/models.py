from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    menu_name = models.CharField(max_length=100,default='main_menu')
    def __str__(self):
        return self.name

