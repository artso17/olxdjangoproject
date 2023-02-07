# Import libraries
from django.contrib import admin
from django.urls import path
from .apps import views

# navigator link-link
urlpatterns = [
    # link menuju administrasi django
    path('admin/', admin.site.urls),
    
    # Link untuk mengeksekusi fungsi predict_form_view
    path("", views.predict_form_view, name="form1"),
    
    # Link untuk mengeksekusi fungsi predict_list_view 
    path("result", views.predict_list_view, name="result")
]
