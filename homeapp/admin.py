from django.contrib import admin
from .models import Card_Model, Blog_Model, ContactModel

admin.site.register(Card_Model)
# admin.site.register(Blog_Model)

admin.site.register(ContactModel)
# subscribe model register

@admin.register(Blog_Model)

class Blog_Model(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)



