from django.db import models
from django.utils import timezone

# Create your models here.

class TipoAgenda(models.Model):
    tipo = models.CharField('Tipo de Agenda',max_length=20)
    def __str__(self):
        return self.tipo

class Usuario(models.Model):
    nome = models.CharField('usuario',max_length=200)
    senha = models.CharField('senha', max_length=100)

    def __str__(self):
        return self.nome
        

class Agenda(models.Model):
    visivel = models.BooleanField('Visibilidade', default=True)
    usuario = models.ForeignKey(Usuario)
    tipoAgenda = models.ForeignKey(TipoAgenda)
    institucional = models.BooleanField('Institucional', default=True)
    compartilhar = models.BooleanField('Compartilhar', default=True)

    


class Compromisso(models.Model):
    evento = models.CharField('nome do Evento', max_length=100)
    dataEHoraDeInicio = models.DateTimeField('hora e data Inicio',default=timezone.now)
    dataEHoraDeFim = models.DateTimeField('hora e data Fim',default=timezone.now)
    onde = models.CharField('endereco',max_length=200)
    agenda = models.ForeignKey(Agenda)
    usuario = models.ForeignKey(Usuario, null = True, blank=False)

    def __str__(self):
        return self.evento + str(self.dataEHoraDeInicio) + str(self.dataEHoraDeFim) + self.onde

class AgendaUsuario(object):
    agenda=models.ForeignKey(Agenda)
    usuario=models.ForeignKey(Usuario)

class UsuarioCompromisso(object):
    Compromisso=models.ForeignKey(Compromisso)
    usuario=models.ForeignKey(Usuario)


class Convite(models.Model):
    responsavel = models.ForeignKey(Usuario, related_name='responsavel')
    Compromisso = models.ForeignKey(Compromisso, related_name='compromisso')
    convidado = models.ForeignKey(Usuario, related_name='convidado')
    status = models.CharField(max_length=50, choices=[('pendente', 'pendente'), ('aceito', 'aceito'), ('negado', 'negado')], default='pendente')
    
    

        



    #def __str__(self):
        #return self.evento + " D_Inicio: " + self.dataEHoraDeInicio + " D_Fim: " + self.dataEHoraDeFim + " Onde: " + self.onde





    #def __str__(self):
        #return self.data + "(" + self.nomeFeriado + ")"
