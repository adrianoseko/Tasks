from django.db import models

class Propostas(models.Model):
    full_name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    address = models.TextField()
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.full_name