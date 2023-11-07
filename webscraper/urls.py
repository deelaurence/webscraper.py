# myapp/urls.py
from django.urls import path
from .views import JobListingViewSet
from . import views

urlpatterns = [
    path('scrapes/', JobListingViewSet.as_view(), name='scrapes'),
    # path('scrapes/', views.get, name='scrapes'),
]
