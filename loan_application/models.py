from django.db import models
from django.contrib.auth.models import User

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


class Phone(models.Model):
    phone_country_area = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    phone_extention = models.CharField(max_length=100)
    phone_type = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)


class Address(models.Model):
    address_line = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address_type = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    address_reference = models.TextField()
    address_since_date = models.DateField(auto_now=True, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_rnc = models.CharField(max_length=100, null=True, blank=True)
    company_email = models.EmailField(max_length=100, null=True, blank=True)
    company_type = models.CharField(max_length=100, null=True, blank=True)
    date_founded = models.DateField(auto_now=True, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)
    # class Meta:
    #  verbose_name_plural = "companies"

    # def __str__(self) -> str:
    #    return f"{self.company_name}"


class SuscriberCompany(models.Model):
    suscriber_id = models.ForeignKey(Suscriber, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)


class Branch(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=100)
    branch_description = models.TextField(null=True, blank=True)
    is_main_branch = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)


class Branch(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=100)
    branch_description = models.TextField(null=True, blank=True)
    is_main_branch = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)


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
    department_name = models.CharField(max_length=100)
    departmen_description = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(auto_now=True, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    marital_status = models.CharField(max_length=100, null=True, blank=True)
    educational_level = models.CharField(max_length=100, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)



class PersonAddress(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)


class PersonPhone(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    NID = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)