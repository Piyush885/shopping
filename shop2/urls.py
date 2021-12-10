from django.contrib import admin
from django.urls import path,include
from shop2 import views

urlpatterns = [
    path('',views.home,name='home'),
    path('adminpage',views.adminpage,name='admin'),
    path('userpage',views.userpage,name='user'),
    path('adminvalidate',views.adminvalidate,name='adminvalidate'),
    path('uservalidate',views.uservalidate,name='uservalidate'),
    path('additems',views.additems,name='additems'),
    path('update',views.update,name='update'),
    path('delete',views.delete,name='delete'),
    path('addtocart/<str:pname>/<str:price>/<str:name>',views.addtocart,name='addtocart'),
    path('showcart/<str:name>',views.showcart,name='showcart'),
    path('cartremove/<str:pname>/<str:name>',views.cartremove,name='cartremove'),
    path('newuserpage',views.newuserpage,name='newuserpage'),
    path('usersave',views.usersave,name='usersave'),
]