# Generated by Django 5.1.4 on 2025-04-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorados',
            name='estagios',
            field=models.CharField(choices=[('I', 'Iniciante'), ('M', 'Intermediário'), ('A', 'Avançado')], max_length=2),
        ),
    ]
