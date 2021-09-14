from django.contrib import admin
from .models import Word



class WordAdmin(admin.ModelAdmin):
    list_display = ['word_text', 'tf_amount', 'idf_amount']

admin.site.register(Word, WordAdmin)
