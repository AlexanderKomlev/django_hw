# Generated by Django 5.0.1 on 2024-01-15 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_remove_student_teacher_student_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]
