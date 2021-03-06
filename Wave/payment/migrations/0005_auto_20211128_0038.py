# Generated by Django 3.2.7 on 2021-11-28 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_payment_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='reference',
            field=models.CharField(default='bLtq7iEJ-vIhAYQ-NPvdY1DY4H1YC8DHrGaeo7oGLtPiNmsAWItLMjuirbVzbWse5Hc', max_length=100),
        ),
    ]
