from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.readandinsert,name = "add"),
    path('del/<int:id>/',views.destroy,name = "del"),
    path('/<int:id>/',views.modify,name = "modifys"),
   
]