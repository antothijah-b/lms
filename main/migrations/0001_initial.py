# Generated by Django 4.2.5 on 2023-09-14 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryID', models.BigAutoField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructorID', models.BigAutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('contactNumber', models.CharField(max_length=10)),
                ('verificationStatus', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.BigAutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('contactNumber', models.CharField(max_length=10)),
                ('verificationStatus', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollments',
            fields=[
                ('enrollmentID', models.BigAutoField(primary_key=True, serialize=False)),
                ('enrollmentDate', models.DateField()),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseID', models.BigAutoField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('enrollmentCapacity', models.IntegerField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('categoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('intructorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.instructor')),
            ],
        ),
    ]
