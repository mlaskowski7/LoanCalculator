from django.db import models

# Create your models here.

class Loan(models.Model):
    title = models.CharField(primary_key= True, max_length=200)
    value = models.FloatField(default=0)
    lending_rate = models.FloatField(default=0)
    months = models.FloatField(default=12)

    def calculate_paid_value(self):
        return self.value + self.value * self.lending_rate

    def calculate_monthly_instalment(self):
        return self.calculate_paid_value() / self.months

    def calculate_overpayment(self):
        return self.calculate_paid_value() - self.value

    def __str__(self):
        return self.title