from  django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),

    path('las_flores', views.capullo, name='las_flores'),
    path('las_flores/crear', views.crea_capullo, name='crear'),
    path('las_flores/editar', views.editar_capullo, name='editar'),
    path('eliminar/<int:id>', views.eliminar_capullo, name="eliminar"),
    path('las_flores/editar/<int:pk>', views.editar_capullo, name="editar")

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)