# Generated by Django 5.0.1 on 2024-01-15 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('resume', models.FileField(upload_to='pdfs/')),
                ('position', models.CharField(choices=[('Front-end developer', 'Front-end developer'), ('Back-end developer', 'Back-end developer'), ('Fullstack developer', 'Fullstack developer'), ('SQL developer', 'Fullstack developer'), ('HR Trainee', 'HR Trainee')], max_length=50)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_date', models.DateField(null=True)),
                ('position', models.CharField(choices=[('Front-end developer', 'Front-end developer'), ('Back-end developer', 'Back-end developer'), ('Fullstack developer', 'Fullstack developer'), ('SQL developer', 'Fullstack developer'), ('HR Trainee', 'HR Trainee')], max_length=30, null=True)),
                ('interviewer', models.CharField(max_length=50, null=True)),
                ('interview_status', models.CharField(choices=[('Interviewed', 'Interviewed'), ('Not Interviewed', 'Not Interviewed'), ('Interview scheduled', 'Interview scheduled'), ('Selected', 'Selected'), ('Not-selected', 'Not-selected'), ('Action-pending', 'Action-pending')], max_length=30, null=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='OFFERS_DETAILS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offers', models.CharField(choices=[('OFFER ACCEPTED', 'OFFER ACCEPTED'), ('OFFER REJECTED', 'OFFER REJECTED')], max_length=30, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.candidate')),
                ('position', models.ForeignKey(max_length=30, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.interview')),
            ],
        ),
    ]
