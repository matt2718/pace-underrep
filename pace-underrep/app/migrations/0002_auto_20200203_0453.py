# Generated by Django 2.2.7 on 2020-02-03 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='circuits',
            field=models.ManyToManyField(blank=True, to='app.Circuit'),
        ),
        migrations.AlterField(
            model_name='person',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='facebook',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='identities',
            field=models.ManyToManyField(blank=True, to='app.Identity'),
        ),
        migrations.AlterField(
            model_name='person',
            name='involvements',
            field=models.ManyToManyField(blank=True, to='app.Involvement'),
        ),
        migrations.AlterField(
            model_name='person',
            name='propic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='person',
            name='visibility',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
    ]
