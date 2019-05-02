from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
	template_name = 'web/index.html'


class InstitucionalView(TemplateView):
	template_name = 'web/institucional.html'


class GaleriaView(TemplateView):
	template_name = 'web/galeria.html'


class TeoriaView(TemplateView):
	template_name = 'web/teoria.html'


class DocentesView(TemplateView):
	template_name = 'web/docentes.html'