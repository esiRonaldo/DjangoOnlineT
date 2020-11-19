from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

#1st approach
# Create your views here.
# def index(request):
#   return render(request,'index.html')

#2nd approach
#class CBView(View):
 #   def get(self, request):
  #      return HttpResponse("Class based Views")

#3rd and best approach
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['injectme']='BASIC INJECTION!'
        return context