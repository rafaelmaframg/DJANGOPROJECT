# Generated by Django 3.2.2 on 2021-05-09 15:52
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
