# Generated by Django 3.2.18 on 2023-04-06 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20230327_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('assessmentID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('assessmentType', models.CharField(max_length=20)),
                ('assessmentWeight', models.IntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('lecturerID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('lecturerName', models.CharField(max_length=100)),
                ('lecturerEmail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('moduleID', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('moduleName', models.CharField(max_length=100)),
                ('moduleSemester', models.IntegerField(default=3)),
                ('moduleDescription', models.CharField(max_length=250)),
                ('moduleLevel', models.IntegerField(default=1)),
                ('moduleWeight', models.IntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='ModuleLecturer',
            fields=[
                ('moduleLecturerID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('lectureID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.lecturer')),
                ('moduleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.module')),
            ],
        ),
        migrations.CreateModel(
            name='ModulePathway',
            fields=[
                ('modulePathwayID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('mpType', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Pathway',
            fields=[
                ('pathwayID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('pathwayName', models.CharField(max_length=100)),
                ('pathwayLevels', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.IntegerField(primary_key=True, serialize=False)),
                ('currentPathwayMark', models.IntegerField(default=100)),
                ('courseID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.pathway')),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('studentInfoID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('stuInfoPassword', models.CharField(max_length=50)),
                ('stuInfoName', models.CharField(default='temp', max_length=100)),
                ('stuInfoEmail', models.EmailField(max_length=254)),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentInterest',
            fields=[
                ('studentInterestID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('interestName', models.CharField(max_length=100)),
                ('interestImportantce', models.IntegerField(default=0)),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentModule',
            fields=[
                ('studentModuleID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('stuModMark', models.IntegerField(default=100)),
                ('moduleID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.module')),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.student')),
            ],
        ),
        migrations.RemoveField(
            model_name='modulecourse',
            name='courseRef',
        ),
        migrations.RemoveField(
            model_name='modulecourse',
            name='moduleRef',
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.DeleteModel(
            name='moduleCourse',
        ),
        migrations.DeleteModel(
            name='Modules',
        ),
        migrations.AddField(
            model_name='modulepathway',
            name='courseID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.pathway'),
        ),
        migrations.AddField(
            model_name='modulepathway',
            name='moduleID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.module'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='moduleID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.module'),
        ),
    ]
