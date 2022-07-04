from django.db import models

# Create your models here.
class Test(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    zakaz_field = models.CharField(db_column='заказ_№', max_length=40)
    stoimostvdol_field = models.IntegerField(db_column='стоимость_в_$', blank=True, null=True)
    srok_postavki = models.CharField(db_column='срок_поставки', max_length=30, blank=True, null=True)
    stoimostvrub = models.IntegerField(db_column='стоимость_в_rub', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'