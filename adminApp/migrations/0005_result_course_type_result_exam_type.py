# Generated by Django 4.2.6 on 2023-10-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0004_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='course_type',
            field=models.CharField(choices=[('Lab', 'Lab'), ('Theory', 'Theory')], default='Theory', max_length=6),
        ),
        migrations.AddField(
            model_name='result',
            name='exam_type',
            field=models.CharField(choices=[('Mid', 'Mid'), ('Sem', 'Sem')], default='Mid', max_length=4),
        ),
    ]
