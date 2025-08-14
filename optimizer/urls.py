

from django.urls import path

from . import views

from django.urls import re_path as url

from django.http import HttpResponse
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('optimize-route/', views.optimize_route_view, name='optimize_route_view'),
    path('data-source/', views.data_source_table_view, name='data_source_table_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
