from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Phone(models.Model):
    phone_country_area = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    phone_extention = models.CharField(max_length=100)
    phone_type = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "phones"

    def __str__(self) -> str:
        return f"Phone: {self.phone_number}"


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

    class Meta:
        verbose_name_plural = "addresses"

    def __str__(self) -> str:
        return f"{self.address_line}"


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

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class PersonAddress(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)


class PersonPhone(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_id = models.ForeignKey(Phone, on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    NID = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "roles"

    def __str__(self) -> str:
        return f"{self.name}"


class UserRole(models.Model):
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "users_roles"


class Permission(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "permissions"

    def __str__(self) -> str:
        return f"{self.name}"


class RolePermission(models.Model):
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission_id = models.ForeignKey(Permission, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "roles_permissions"
