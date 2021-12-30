from django.contrib import admin
from .models import Buy_Now

# Register your models here.
class Buy_NowAdmin(admin.ModelAdmin):
    list_display = ('id','Current_TotalBallance_In_Wallet','CryptoName','Buying_Price','Ammount','TimeAndDate')

admin.site.register(Buy_Now,Buy_NowAdmin)