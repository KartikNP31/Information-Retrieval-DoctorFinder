from django.urls import path
from .views import index
from .views import search
from .views import showPR_curve

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
    path('showPR_curve/', showPR_curve, name='showPR_curve'),
]