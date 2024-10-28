from django.urls import path
from .views import *

urlpatterns = [
    path('experiences/', Experiences.as_view(), name='experiences'),
    path('portfolio/', Portfolio.as_view(), name='portfolio'),
]