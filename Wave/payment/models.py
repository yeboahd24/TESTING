from django.db import models
import secrets


class Payment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    currency = models.CharField(max_length=100)
    reference = models.CharField(max_length=100, default=secrets.token_urlsafe(50))
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        while not self.reference:
            reference = secrets.token_urlsafe(50)
            similar_reference = Payment.objects.filter(reference=reference)
            if not similar_reference:
                self.reference = reference
        super().save(*args, **kwargs)


class Music(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title