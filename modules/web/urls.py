from django.urls import path
from .views import (
	IndexView,
	InstitucionalView,
)


app_name = 'web'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('institucional/', InstitucionalView.as_view(), name='institucional'),
]