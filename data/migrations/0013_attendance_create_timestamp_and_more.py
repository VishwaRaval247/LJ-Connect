# Generated by Django 4.1.10 on 2023-07-30 18:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0012_alter_attendance_lecture_no"),
    ]

    operations = [
        migrations.AddField(
            model_name="attendance",
            name="create_timestamp",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Create Timestamp",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="attendance",
            name="update_timestamp",
            field=models.DateTimeField(auto_now=True, verbose_name="Update Timestamp"),
        ),
        migrations.AddField(
            model_name="moocresult",
            name="create_timestamp",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Create Timestamp",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="moocresult",
            name="update_timestamp",
            field=models.DateTimeField(auto_now=True, verbose_name="Update Timestamp"),
        ),
        migrations.AddField(
            model_name="remedialtestresult",
            name="create_timestamp",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Create Timestamp",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="remedialtestresult",
            name="update_timestamp",
            field=models.DateTimeField(auto_now=True, verbose_name="Update Timestamp"),
        ),
        migrations.AddField(
            model_name="studentsemesterrecord",
            name="create_timestamp",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Create Timestamp",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="studentsemesterrecord",
            name="update_timestamp",
            field=models.DateTimeField(auto_now=True, verbose_name="Update Timestamp"),
        ),
        migrations.AddField(
            model_name="testresult",
            name="create_timestamp",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Create Timestamp",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="testresult",
            name="update_timestamp",
            field=models.DateTimeField(auto_now=True, verbose_name="Update Timestamp"),
        ),
    ]
