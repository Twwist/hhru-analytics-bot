from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50, null=True)
    middle_name = fields.CharField(max_length=50, null=True)
    gender = fields.CharField(max_length=10, null=True)
    age = fields.IntField(null=True)
    area = fields.CharField(max_length=100, null=True)
    certificate = fields.CharField(max_length=255, null=True)
    education_level = fields.CharField(max_length=50, null=True)
    education_primary_name = fields.CharField(max_length=100, null=True)
    education_primary_organization = fields.CharField(max_length=100, null=True)
    education_primary_result = fields.CharField(max_length=100, null=True)
    education_primary_year = fields.IntField(null=True)
    experience_area = fields.CharField(max_length=100, null=True)
    experience_company = fields.CharField(max_length=100, null=True)
    experience_start = fields.DatetimeField(null=True)
    experience_end = fields.DatetimeField(null=True)
    experience_industry = fields.CharField(max_length=100, null=True)
    experience_position = fields.CharField(max_length=100, null=True)
    salary_amount = fields.IntField(null=True)
    salary_currency = fields.CharField(max_length=5, null=True)
    title = fields.CharField(max_length=100, null=True)
    total_experience = fields.IntField(null=True)
    phone = fields.CharField(max_length=20, null=True)
    email = fields.CharField(max_length=100, null=True)
    created_at = fields.DatetimeField(null=True)
    updated_at = fields.DatetimeField(null=True)
