from django.db import models 
from django.contrib.auth import get_user_model

User = get_user_model()

class Contact(models.Model):
       email=models.CharField(max_length=122)
       desc=models.TextField(max_length=250)

class signup(models.Model):
      contact = models.IntegerField(default=False)
      password = models.CharField(max_length = 15)


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
