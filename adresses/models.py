from django.db import models


class Ceps(models.Model):
    cep = models.IntegerField(primary_key=True, unique=True, blank=True)
    city = models.CharField(max_length=300, blank=True,
                            null=True, db_index=True)
    state = models.CharField(max_length=300, blank=True,
                             null=True, db_index=True)
    street = models.CharField(
        max_length=300, blank=True, null=True, db_index=True)

    def __str__(self):
        return str(self.cep)


class States(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    name = models.CharField(max_length=300, blank=True)
    uf = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.uf


class Cities(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    name = models.CharField(max_length=300, blank=True)
    state = models.ForeignKey(States, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
