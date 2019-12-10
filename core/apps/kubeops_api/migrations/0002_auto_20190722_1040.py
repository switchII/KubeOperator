# Generated by Django 2.1.2 on 2019-07-22 10:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storage',
            name='created_by',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='storage',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]