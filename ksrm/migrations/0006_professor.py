# Generated by Django 5.0.6 on 2024-07-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksrm', '0005_delete_log_alter_student1_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('employee_id', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
            ],
        ),
    ]
