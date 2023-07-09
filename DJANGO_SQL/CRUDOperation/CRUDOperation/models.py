from django.db import models

class locationModel(models.Model):
    location_id=models.IntegerField(primary_key=True)
    street_add=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    contry=models.CharField(max_length=200)

    class Meta:
        db_table = 'labor_wages_t18\".\"location'

class dcompanyModel(models.Model):
    company_id=models.IntegerField(primary_key=True)
    company_type=models.CharField(max_length=200)
    street_add=models.CharField(max_length=200)
    highest_no_worker=models.IntegerField(max_length=200)
    region_id=models.IntegerField(max_length=200)
    company_name=models.CharField(max_length=200)

    class Meta:
        db_table = 'labor_wages_t18\".\"company_details'

    