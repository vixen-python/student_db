# Generated by Django 3.0.10 on 2021-07-12 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20210627_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=128)),
                ('house_number', models.CharField(max_length=16)),
                ('zip_code', models.CharField(max_length=16)),
                ('country_iso3', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='permanent_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='student.Address'),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_phone', models.CharField(blank=True, max_length=32)),
                ('personal_phone', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=128)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='student.Student')),
            ],
            options={
                'unique_together': {('student', 'work_phone', 'personal_phone', 'email')},
            },
        ),
    ]
