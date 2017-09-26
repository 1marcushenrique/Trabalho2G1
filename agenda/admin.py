from django.contrib import admin

# Register your models here.

from agenda.models import *

admin.site.register(TipoAgenda)
admin.site.register(Usuario)
admin.site.register(Agenda)
admin.site.register(Compromisso)
