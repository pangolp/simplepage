from django.urls import path
from .views import (
	IndexView,
	InstitucionalView,
	GaleriaView,
	TeoriaView,
	DocentesView,
)


app_name = 'web'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('institucional/autoridades/', InstitucionalView.as_view(), name='institucional'),
    path('galeria/', GaleriaView.as_view(), name='galeria'),
    path('teoria/', TeoriaView.as_view(), name='teoria'),
    path('docentes/', DocentesView.as_view(), name='docentes'),
]