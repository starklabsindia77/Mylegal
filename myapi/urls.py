# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from myapi.views import *




urlpatterns =[
			path('category/', CategoryViews.as_view(), name="Category List"),
			path('IPC/', IPCViews.as_view(), name="IPC List"),			
			]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

