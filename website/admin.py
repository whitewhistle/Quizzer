from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)

class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionsAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

admin.site.register(Questions1 , QuestionsAdmin)
admin.site.register(Answer)
