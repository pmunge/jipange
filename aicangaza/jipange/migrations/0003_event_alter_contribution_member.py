# Generated by Django 5.1.2 on 2024-11-22 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jipange', '0002_contribution_amount_alter_contribution_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('target', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='contribution',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributions_list', to='jipange.member'),
        ),
    ]
