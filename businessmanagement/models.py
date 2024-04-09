from django.db import models
from django.contrib.auth.models import User
#from usermanagement.models import Address, Phone
from usermanagement.models import Address, Phone

# Create your models here.


class Suscriber(models.Model):
    code = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    logo_src = models.CharField(max_length=100, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "suscribers"

    def __str__(self) -> str:
        return f"{self.code}"


class Company(models.Model):
    name = models.CharField(max_length=200)
    rnc = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    date_founded = models.DateField(auto_now=True, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self) -> str:
        return f"{self.company_name}"


class SuscriberCompany(models.Model):
    suscriber_id = models.ForeignKey(Suscriber, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)


class Branch(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    is_main_branch = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "branchs"

    def __str__(self) -> str:
        return f"{self.name}"


class BranchAddress(models.Model):
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)


class BranchPhone(models.Model):
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)


class Department(models.Model):
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "departments"

    def __str__(self) -> str:
        return f"{self.name}"
