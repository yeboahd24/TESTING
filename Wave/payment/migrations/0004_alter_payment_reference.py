# Generated by Django 3.2.7 on 2021-11-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20211126_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='reference',
            field=models.CharField(default='fq7zvFsgHg_Vnjt_wbV0m9BM9vss1bZZ9JeMhyzDIyk2xrv7MMmuj_Nqded-K9pHLvA', max_length=100),
        ),
    ]
