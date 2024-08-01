from django.contrib import admin
from home.models  import Contact
from home.models import Transaction
from home.models import  signup
from home.models import icecream
from home.models import family
from home.models import mf
from home.models import Orders

# Register your models here.
admin.site.register(Contact)
admin.site.register(signup)
admin.site.register(Transaction)
admin.site.register(icecream)
admin.site.register(family)
admin.site.register(mf)
admin.site.register(Orders)
