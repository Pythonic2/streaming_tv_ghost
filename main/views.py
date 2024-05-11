from django.http import HttpRequest
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView, CreateView
from .forms import ClienteForm
from .models import Cliente
from django.urls import reverse_lazy
from .utils import BotChrome

    
def automation(email):
    bot = BotChrome()
    bot.acessar()
    try:
        bot.login(email)
    except Exception as e:
        pass

def htmx_cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        
        if form.is_valid:
            email = request.POST.get('email')
            try:
                teste = form.save(commit=False)
                teste.save()
                print(automation(email))
            except:
                return HttpResponse('Hum... infelizmente esse email ja solicitou um teste.')
            return HttpResponse('Verifique seu Email, as informaçõe do Teste Estarão lá.')
        
    
class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {'form':ClienteForm}
        return render(request, self.template_name,context)
    
    
        