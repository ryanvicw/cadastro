from django.contrib import admin
from . import models

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','idade','email','contato')
    list_filter = ('nome','endereco',)
    search_fields = ('nome',)
    list_per_page=5
    list_editable = ('idade','contato',)
