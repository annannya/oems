# Generated by Django 4.1.4 on 2022-12-29 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Name', models.CharField(max_length=50)),
                ('Department', models.CharField(max_length=50)),
                ('Joining', models.DateField()),
                ('Location', models.CharField(max_length=50)),
                ('Salary', models.IntegerField(default=0)),
                ('Bonus', models.IntegerField(default=0)),
                ('Role', models.CharField(max_length=50)),
                ('Phone_No', models.CharField(max_length=10)),
            ],
        ),
    ]
