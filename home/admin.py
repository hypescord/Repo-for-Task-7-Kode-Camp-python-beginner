from django.contrib import admin
from .models import Person, Addresse, Doctor, Product, Bio

# Register your models here.

admin.site.register(Person)

admin.site.register(Addresse)

admin.site.register(Doctor)

admin.site.register(Product)

admin.site.register(Bio)