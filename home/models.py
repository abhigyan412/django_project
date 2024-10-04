from django.db import models 

from django.contrib.auth import get_user_model

User = get_user_model()

class Contact(models.Model):
       email=models.CharField(max_length=122)
       desc=models.TextField(max_length=250)

class suggestion(models.Model): 
     suggestions = models.TextField(max_length=800 , null=True)
     email=models.CharField(max_length=122 , default=False)      

class signup(models.Model):
      contact  = models.IntegerField(null = False  , default=False)    
      password = models.CharField(max_length = 15)


class icecream(models.Model):
     name = models.CharField(max_length=20)
     image = models.ImageField(upload_to='home/images/')
     price = models.FloatField()

class family(models.Model):
     name = models.CharField(max_length=20)
     image = models.ImageField(upload_to='images/')
     price = models.FloatField()

class mf(models.Model):     
     name = models.CharField(max_length=20)
     image = models.ImageField(upload_to="images/")
     price = models.FloatField()




class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', 
                                on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)


    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)


class Orders(models.Model):
     order_id= models.AutoField(primary_key=True)
     items_json= models.CharField(max_length=5000)
     amount=models.IntegerField(default=0)
     name=models.CharField(max_length=90)
     email=models.CharField(max_length=111)
     address=models.CharField(max_length=111)
     city=models.CharField(max_length=111)
     state=models.CharField(max_length=111)
     zip_code=models.CharField(max_length=111)
     phone=models.CharField(max_length=111 , default="")



     