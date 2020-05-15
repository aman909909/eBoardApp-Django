from django.contrib import admin

from .models import board, nlist, card, cardComment
# Register your models here.


admin.site.register(board)
admin.site.register(nlist)
admin.site.register(card)
admin.site.register(cardComment)