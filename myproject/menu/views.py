from django.shortcuts import render
from menu.models import MenuItem

def my_page_view(request,*args):
    menu_name = 'main_menu'
    return render(request, 'menu/my_page.html', {'menu_name': menu_name})

