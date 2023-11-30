from django.contrib import admin
from accounts import models



@admin.register(models.User)
class user(admin.ModelAdmin):
    model = models.User
    list_display = [
        "id",
        "email",
        "name",
        "surname",
        "phone_number",
        ]
    search_fields = ["name"]
