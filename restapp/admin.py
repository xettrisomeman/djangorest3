from django.contrib import admin

from .models import (
    CustomUser,
    Book,
    Author
)

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(CustomUser)