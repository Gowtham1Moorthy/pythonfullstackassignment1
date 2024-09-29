# Generated by Django 4.1.2 on 2022-11-16 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat_list',
            fields=[
                ('category', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.PositiveIntegerField()),
                ('customer', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('reason', models.CharField(max_length=500)),
                ('at', models.DateTimeField()),
                ('number', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Lang_list',
            fields=[
                ('language', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='plat_list',
            fields=[
                ('platform', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Views',
            fields=[
                ('v_id', models.FloatField(primary_key=True, serialize=False)),
                ('sum', models.FloatField()),
                ('count', models.PositiveIntegerField()),
                ('on_what', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('web_id', models.FloatField(primary_key=True, serialize=False)),
                ('w_name', models.CharField(max_length=50)),
                ('release_year', models.PositiveIntegerField()),
                ('seasons', models.PositiveIntegerField()),
                ('rating', models.FloatField(blank=True, null=True)),
                ('studio', models.CharField(max_length=30)),
                ('ageplus', models.PositiveIntegerField()),
                ('portrait', models.ImageField(upload_to='static/upload')),
                ('landscape', models.ImageField(upload_to='static/upload')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('episodes', models.PositiveIntegerField()),
                ('release_year', models.PositiveIntegerField()),
                ('rating', models.FloatField(blank=True, null=True)),
                ('sea_id', models.FloatField(primary_key=True, serialize=False)),
                ('web_id', models.ForeignKey(db_column='web_id', on_delete=django.db.models.deletion.CASCADE, to='ottratings.web')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('e_name', models.CharField(max_length=100)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('run_time', models.TimeField()),
                ('epi_id', models.FloatField(primary_key=True, serialize=False)),
                ('sea_id', models.ForeignKey(db_column='sea_id', on_delete=django.db.models.deletion.CASCADE, to='ottratings.season')),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('rating', models.FloatField()),
                ('rorb_id', models.AutoField(primary_key=True, serialize=False)),
                ('rby', models.ForeignKey(db_column='rby', on_delete=django.db.models.deletion.CASCADE, to='ottratings.users')),
                ('ron', models.ForeignKey(db_column='ron', on_delete=django.db.models.deletion.CASCADE, to='ottratings.views')),
            ],
            options={
                'unique_together': {('ron', 'rby')},
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('lwll_id', models.AutoField(primary_key=True, serialize=False)),
                ('language', models.ForeignKey(db_column='language', on_delete=django.db.models.deletion.CASCADE, to='ottratings.lang_list')),
                ('web_id', models.ForeignKey(db_column='web_id', on_delete=django.db.models.deletion.CASCADE, to='ottratings.web')),
            ],
            options={
                'unique_together': {('web_id', 'language')},
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('tag', models.PositiveIntegerField()),
                ('c', models.CharField(max_length=100)),
                ('cat', models.DateTimeField()),
                ('cocb_id', models.AutoField(primary_key=True, serialize=False)),
                ('cby', models.ForeignKey(db_column='cby', on_delete=django.db.models.deletion.CASCADE, to='ottratings.users')),
                ('con', models.ForeignKey(db_column='con', on_delete=django.db.models.deletion.CASCADE, to='ottratings.views')),
            ],
            options={
                'unique_together': {('con', 'cby', 'cat')},
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('cwcc_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.ForeignKey(db_column='category', on_delete=django.db.models.deletion.CASCADE, to='ottratings.cat_list')),
                ('web_id', models.ForeignKey(db_column='web_id', on_delete=django.db.models.deletion.CASCADE, to='ottratings.web')),
            ],
            options={
                'unique_together': {('web_id', 'category')},
            },
        ),
        migrations.CreateModel(
            name='Available_on',
            fields=[
                ('avap_id', models.AutoField(primary_key=True, serialize=False)),
                ('platform', models.ForeignKey(db_column='platform', on_delete=django.db.models.deletion.CASCADE, to='ottratings.plat_list')),
                ('web_id', models.ForeignKey(db_column='web_id', on_delete=django.db.models.deletion.CASCADE, to='ottratings.web')),
            ],
            options={
                'unique_together': {('web_id', 'platform')},
            },
        ),
    ]
