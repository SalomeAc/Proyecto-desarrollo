from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home,name='home'),
    path('login/', views.login, name='login'),
    path('administrador/', views.adminInicio, name='Admin'),
    path('administrador/categorias/', views.adminPrueba, name='Categorias'),
    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)