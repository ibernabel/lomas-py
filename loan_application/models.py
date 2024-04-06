from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class suscribers(models.Model):
  code = models.CharField(max_length=100)
  name = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  rnc = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  owner = models.CharField(max_length=100)
  logo_src = models.CharField(max_length=100)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(null=True, blank=True)
  update_by = models.ForeignKey(User, on_delete=models.CASCADE)