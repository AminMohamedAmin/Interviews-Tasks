from django.contrib import admin
from .models import file

# Register your models here.

class fileAdmin(admin.ModelAdmin):
	list_display = ["username","job","level","file"]

admin.site.register(file,fileAdmin)


#user :admin
#pass :admin