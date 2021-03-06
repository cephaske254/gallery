from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('cat/<category>/',views.index, name='category'),
    path('pin/<location>/',views.index, name='location'),
    path('search/',views.search_results, name='search'),
    path('copy_link/<int:id>',views.copy_link, name='copy_link'),
    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
