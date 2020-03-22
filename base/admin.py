from django.contrib import admin

from .models import board, nlist, card
# Register your models here.


admin.site.register(board)
admin.site.register(nlist)
admin.site.register(card)