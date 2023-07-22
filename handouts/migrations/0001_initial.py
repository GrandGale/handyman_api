# Generated by Django 4.2.3 on 2023-07-22 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import handouts.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(db_index=True, max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Department')),
                ('abbrev', models.CharField(max_length=10, unique=True, verbose_name='Abbreviation')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Faculty')),
                ('abbrev', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='Abbreviation')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnderGradLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbrev', models.CharField(db_index=True, max_length=10, unique=True)),
                ('level', models.CharField(max_length=4, unique=True)),
            ],
            options={
                'verbose_name': 'UnderGraduate Level',
                'verbose_name_plural': 'UnderGraduate Levels',
            },
        ),
        migrations.CreateModel(
            name='Handout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=handouts.utils.get_handout_upload_path)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='handouts.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='handouts.department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='handouts.faculty')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handouts.session')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Handout',
                'verbose_name_plural': 'Handouts',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='handouts.faculty', verbose_name='Faculty'),
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='handouts.undergradlevel'),
        ),
    ]