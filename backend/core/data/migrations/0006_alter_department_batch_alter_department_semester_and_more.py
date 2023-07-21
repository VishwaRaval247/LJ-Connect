# Generated by Django 4.1.10 on 2023-07-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_merge_20230714_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='batch',
            field=models.ManyToManyField(blank=True, to='data.batch', verbose_name='Batch'),
        ),
        migrations.AlterField(
            model_name='department',
            name='semester',
            field=models.CharField(help_text='e.g. 1', max_length=1, verbose_name='Semester'),
        ),
        migrations.AlterField(
            model_name='department',
            name='study_resources',
            field=models.ManyToManyField(blank=True, to='data.studyresource', verbose_name='Study Resources'),
        ),
        migrations.AlterField(
            model_name='studentsemesterrecord',
            name='MOOC_courses',
            field=models.ManyToManyField(blank=True, to='data.moocresult', verbose_name='MOOC Courses'),
        ),
        migrations.AlterField(
            model_name='studentsemesterrecord',
            name='group_project',
            field=models.ManyToManyField(blank=True, to='data.groupproject', verbose_name='Group Project'),
        ),
        migrations.AlterField(
            model_name='studentsemesterrecord',
            name='individual_project',
            field=models.ManyToManyField(blank=True, to='data.individualproject', verbose_name='Individual Project'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='remedial_result',
            field=models.ManyToManyField(blank=True, to='data.remedialtestresult', verbose_name='Remedial Result'),
        ),
    ]
