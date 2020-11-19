from django.shortcuts import render
from . import forms
from django.core import validators


# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.validationError("NAME NEEDS TO START WITH Z")


def form_name_view(request):
    form = forms.FormName()

    if form.is_valid():
        print("VALIDATION SUCCESS!")
        print("NAME: " + form.cleaned_data['name'])
        print("EMAIL: " + form.cleaned_data['email'])
        print("TEXT: " + form.cleaned_data['text'])
        """***botcatcher=forms.CharField(required=False, widget=forms.HiddenInput)
        def clean_botcatcher(self):
            botcatcher=self.cleaned_data['botcatcher']
            if len(botcatcher)>0:
                raise forms.validagtionError("GOTCHA BOT")
            return botcatcher
        """
    return render(request, 'basicapp/from_page.html')
    # return render(request, 'basicapp/form_page.html',{'form':form})
