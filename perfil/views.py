from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

from . import models
from . import forms

class BasePerfi(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if self.request.user.is_authenticated:
            self.contexto ={
                'userform':forms.UserForm(
                    data=self.request.POST or None,
                    usuario=self.request.user,
                    instance=self.request.user
                ),
                'perfilform':forms.PerfilForm(
                    data=self.request.POST or None
                )
            }
        else:
            self.contexto ={
                'userform':forms.UserForm(
                    data=self.request.POST or None
                ),
                'perfilform':forms.PerfilForm(
                    data=self.request.POST or None
                )
            }
        
        self.renderizar = render(
            self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar



class Criar(BasePerfi):
    def post(self, *args, **kwargs):
        return self.renderizar


class Atualizar(View):
    pass


class Login(View):
    pass


class Logout(View):
    pass
