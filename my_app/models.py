from django.db import models

class Hudud(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi

class Kompaniya(models.Model):
    nomi = models.CharField(max_length=100)
    izoh = models.TextField()
    tashkil_topgan = models.DateField(auto_now_add=True)
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nomi
    
class Bino(models.Model):
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)
    kompaniya = models.ForeignKey(Kompaniya, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=100)
    maydoni = models.PositiveIntegerField(null=True, blank=True),
    qavat = models.PositiveIntegerField(),
    parkovka = models.BooleanField(default=False)
    bolalar_maydonchasi = models.BooleanField(default=False),
    lift = models.BooleanField(default=False)
    



