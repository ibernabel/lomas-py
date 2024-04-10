from django.db import models
from django.contrib.auth.models import User
# from usermanagement.models import Address, Phone
from usermanagement.models import Address, Phone, UserProfile, Person

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
        db_table = "suscribers"

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
        db_table = "companies"

    def __str__(self) -> str:
        return f"{self.name}"


class SuscriberCompany(models.Model):
    suscriber = models.OneToOneField(Suscriber, on_delete=models.CASCADE)
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
        db_table = "branchs"

    def __str__(self) -> str:
        return f"{self.name}"


class BranchAddress(models.Model):
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)

    class Meta:
        db_table = "branchs_addresses"


class BranchPhone(models.Model):
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)

    class Meta:
        db_table = "branchs_phones"


class Department(models.Model):
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)

    class Meta:
        db_table = "departments"

    def __str__(self) -> str:
        return f"{self.name}"


class UserDepartment(models.Model):
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)

    class Meta:
        db_table = "users_departments"


class Seller(models.Model):
  user_id = models.OneToOneField(User, on_delete=models.CASCADE)
  seller_level = models.CharField(max_length=100, null=True, blank=True)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(null=True, blank=True)
  update_by = models.CharField(max_length=100)

  class Meta:
      db_table = "sellers"


class Portfolio(models.Model):
  seller_id = models.OneToOneField(Seller, on_delete=models.DO_NOTHING)
  name = models.CharField(max_length=100)
  description = models.TextField(null=True, blank=True)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(null=True, blank=True)
  update_by = models.CharField(max_length=100)

  class Meta:
      db_table = "portfolios"


class Promoter(models.Model):
  person_id = models.OneToOneField(Person, on_delete=models.CASCADE)
  NID = models.CharField(max_length=100)
  bonus_type = models.CharField(max_length=100)
  bonus = models.FloatField()
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(null=True, blank=True)
  update_by = models.CharField(max_length=100)

  class Meta:
      db_table = "promoters"
      

class Customer(models.Model):
  person_id = models.OneToOneField(Person, on_delete=models.CASCADE)
  portfolio_id = models.ForeignKey(Portfolio, on_delete=models.DO_NOTHING)
  NID = models.CharField(max_length=100)
  email = models.EmailField(max_length=100, null=True, blank=True)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(null=True, blank=True)
  update_by = models.CharField(max_length=100)

  class Meta:
      db_table = "customers"
      


