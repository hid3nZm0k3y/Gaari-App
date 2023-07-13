from django.contrib import admin
from .models import Make, Autos, Review, Message

# Register your models here.


admin.site.register(Make)
admin.site.register(Autos)
admin.site.register(Review)
admin.site.register(Message)