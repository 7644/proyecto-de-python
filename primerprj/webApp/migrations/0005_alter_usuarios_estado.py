# Generated by Django 3.2.2 on 2021-06-25 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0004_auto_20210625_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='estado',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webApp.estado'),
        ),
    ]