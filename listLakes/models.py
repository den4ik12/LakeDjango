from django.db import models


class Lake(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250, db_index=True)
    location = models.CharField(verbose_name="Местоположение", max_length=500)
    bassin_area = models.CharField(verbose_name="Бассейновый округ", max_length=500)
    river_bassin = models.CharField(verbose_name="Речной бассейн", max_length=500)
    area = models.FloatField(verbose_name="Площадь")

    class Meta:
        verbose_name = "Озеро"
        verbose_name_plural = "Озера"

    def __str__(self):
        return self.title
