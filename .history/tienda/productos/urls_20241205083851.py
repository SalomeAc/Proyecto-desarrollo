from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import  routers


router=routers.DefaultRouter()

router.register(r'productos',views.ProductoView,'productos')


urlpatterns = [

    path("api/",include(router.urls)),
    path("api/filter_products/", views.search_products),
    
    

    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

