from django.contrib import admin
from .models import Word, Dict, TempD, Idf



class WordAdmin(admin.ModelAdmin):
    list_display = ['word_text', 'tf_amount', 'idf_amount']

admin.site.register(Word, WordAdmin)
admin.site.register(Dict)
admin.site.register(TempD)
admin.site.register(Idf)