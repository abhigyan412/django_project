from django.contrib import admin
from home.models  import Contact
from home.models import Transaction
from home.models import  signup

# Register your models here.
admin.site.register(Contact)
admin.site.register(signup)
admin.site.register(Transaction)