from django.contrib import admin

# import the model
from .models import Todo


class TodoAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ('title', 'description', 'completed')


admin.site.register(Todo, TodoAdmin)
