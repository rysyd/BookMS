# Generated by Django 2.2 on 2019-05-30 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookMS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('publisher', models.CharField(max_length=32)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
