from django.db import models

class Signup(models.Model):
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    user_phone_no = models.CharField(max_length=15, unique=True)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=100)
    user_confirm_password = models.CharField(max_length=100)
    user_Aadhar = models.CharField(max_length=12, unique=True)
    user_location = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.user_first_name} {self.user_last_name}"




