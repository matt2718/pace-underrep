# Generated by Django 2.2.7 on 2020-02-03 06:09

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('tag_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Tag')),
            ],
            bases=('app.tag',),
        ),
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('tag_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Tag')),
            ],
            bases=('app.tag',),
        ),
        migrations.CreateModel(
            name='Involvement',
            fields=[
                ('tag_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Tag')),
            ],
            bases=('app.tag',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.CharField(max_length=200)),
                ('created', models.DateField(auto_now_add=True)),
                ('date_of_birth', models.DateTimeField()),
                ('bio', models.TextField()),
                ('propic', models.ImageField(upload_to='')),
                ('visibility', models.PositiveSmallIntegerField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('circuits', models.ManyToManyField(to='app.Circuit')),
                ('identities', models.ManyToManyField(to='app.Identity')),
                ('involvements', models.ManyToManyField(to='app.Involvement')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
            managers=[
                ('people', django.db.models.manager.Manager()),
            ],
        ),
    ]