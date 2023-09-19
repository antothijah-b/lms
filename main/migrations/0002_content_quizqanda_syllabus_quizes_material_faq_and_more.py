# Generated by Django 4.2.5 on 2023-09-16 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('contentID', models.BigAutoField(primary_key=True, serialize=False)),
                ('contentTitle', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('uploadDate', models.DateField()),
                ('totalViews', models.IntegerField()),
                ('intructorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='QuizQAndA',
            fields=[
                ('quizQAndAID', models.BigAutoField(primary_key=True, serialize=False)),
                ('quizQuestion', models.CharField(max_length=200)),
                ('quizAnswer', models.CharField(max_length=200)),
                ('optionA', models.CharField(max_length=200)),
                ('optionB', models.CharField(max_length=200)),
                ('optionC', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('syllabusID', models.BigAutoField(primary_key=True, serialize=False)),
                ('syllabusTitle', models.CharField(max_length=100)),
                ('topic', models.TextField()),
                ('chapters', models.CharField(max_length=100)),
                ('courseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
            ],
        ),
        migrations.CreateModel(
            name='Quizes',
            fields=[
                ('quizID', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('maxScore', models.IntegerField()),
                ('userScore', models.IntegerField()),
                ('time', models.TimeField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('courseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('instructorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.instructor')),
                ('quizQAndAID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.quizqanda')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('materialID', models.BigAutoField(primary_key=True, serialize=False)),
                ('materialTitle', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('uploadDate', models.DateField()),
                ('contentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.content')),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('faqID', models.BigAutoField(primary_key=True, serialize=False)),
                ('questions', models.TextField()),
                ('answer', models.TextField()),
                ('courseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='syllabusID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.syllabus'),
        ),
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('classID', models.BigAutoField(primary_key=True, serialize=False)),
                ('classTitle', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('classDate', models.DateField()),
                ('classTime', models.TimeField()),
                ('duration', models.DurationField()),
                ('courseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('instructorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.instructor')),
            ],
        ),
    ]
