# Generated by Django 2.2 on 2020-08-03 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_page_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestStandingsHolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problems', models.TextField()),
                ('runs_list', models.TextField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standings_holder', to='courses.Contest')),
            ],
        ),
    ]
