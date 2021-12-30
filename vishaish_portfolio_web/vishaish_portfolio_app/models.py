from django.db import models

# Create your models here.

#Buy CryptoCurrency Fo rTrading Modal

class Buy_Now(models.Model):
    id = models.BigAutoField(primary_key=True)
    Current_TotalBallance_In_Wallet = models.IntegerField()
    CryptoName = models.CharField(max_length=40)
    Buying_Price = models.FloatField()
    Ammount = models.FloatField()
    TimeAndDate= models.DateTimeField(auto_now_add=True,null = True,)