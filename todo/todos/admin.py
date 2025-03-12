from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):  # to make it customizable, extendable
    list_display = [
        "title",
        "body",
    ]

    search_fields = [
        "title",
        "body",
    ]
    list_filter = [
        "title",
        "body",
    ]


admin.site.register(Todo, TodoAdmin)
