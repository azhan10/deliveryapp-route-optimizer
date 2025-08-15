
from django.urls import re_path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	re_path(r'optimize-route/?$', views.optimize_route_view, name='optimize_route_view'),
	re_path(r'data-source/?$', views.data_source_table_view, name='data_source_table_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
