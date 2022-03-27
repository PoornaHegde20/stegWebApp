from django.contrib import admin
from steg.models import LSBEncode
# Register your models here.
admin.site.register(LSBEncode)
from steg.models import LSBDecode
admin.site.register(LSBDecode)
