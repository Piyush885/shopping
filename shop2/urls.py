from django.contrib import admin
from django.urls import path,include
from shop2 import views
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
urlpatterns = [
    path('',views.home,name='home'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('adminpage',views.adminpage,name='admin'),
    # path('userpage',views.userpage,name='user'),
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
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  