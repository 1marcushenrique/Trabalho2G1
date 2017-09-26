from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import *

# Create your views here.


def home(request):
  html = """<h1>Opções</h1>
                    <ul>
                        <li><a href='/agenda'>Agenda</a></li>
                        <li><a href='/compromisso'>Compromisso</a></li>
                        <li><a href='/usuario/'>Usuario</a></li>
                        <li><a href='/tipoAgenda/'>Tipo de Agenda</a></li>


                    </ul>
                """
  return HttpResponse(html)

def tipoAgenda(request):
    retorno = "<h1>Tipo de Usuario</h1>"
    lista = TipoAgenda.objects.all()
    for ev in lista:
        retorno += "Nome do Tipo de Agenda:<li>{}</li>".format(ev.tipo)
        return HttpResponse(retorno)

       


def usuario(request):
    retorno = "<h1>Usuario</h1>"
    lista = Usuario.objects.all()
    for ev in lista:
        retorno += "Nome do Usuario:<li>{}</li>".format(ev.nome)
        return HttpResponse(retorno)

def compromisso(request):
    retorno = "<h1>compromisso</h1>"
    lista = Compromisso.objects.all()
    for ev in lista:
        retorno += "Nome do Evento:<li>{}{}{}{}{}</li>".format(ev.evento, ev.dataEHoraDeInicio, ev.dataEHoraDeFim, ev.onde, ev.agenda)
        return HttpResponse(retorno)

def agenda(request):
  html = "<h1>Agendas </h1>"
  lista = Agenda.objects.all()
  for a in lista:
    html += '<li>{} | {} | {} | {}|</li>'.format(a.visivel,a.usuario, a.tipoAgenda, a.institucional)

  return HttpResponse(html)

