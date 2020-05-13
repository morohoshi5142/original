from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Question)
admin.site.register(Kanmusu)
admin.site.register(Choice)
admin.site.register(Eshi)
admin.site.register(Kansyu)
admin.site.register(Seiyu)
admin.site.register(Oogata)
admin.site.register(Battle)
admin.site.register(Sanka_kanmusu)
admin.site.register(Kansyu_setumei)
admin.site.register(Ivent)
admin.site.register(Tokkokanmusu)
admin.site.register(Ivent_naiyou)
admin.site.register(Playnikki)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(PlayQuestion)
admin.site.register(Answer)
admin.site.register(Like)
admin.site.register(Kannmusu_like)
