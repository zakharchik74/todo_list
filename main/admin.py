from django.contrib import admin

from .models import ToDo, ToDo_completed, ToDo_process

admin.site.register(ToDo)
admin.site.register(ToDo_process)
admin.site.register(ToDo_completed)