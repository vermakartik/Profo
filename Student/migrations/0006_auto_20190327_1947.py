# Generated by Django 2.1.7 on 2019-03-27 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CTest', '0001_initial'),
        ('Student', '0005_auto_20190323_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CTest.Answer')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CTest.Question')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.StudentSummaryModel')),
            ],
        ),
        migrations.AddField(
            model_name='studenttestmodel',
            name='attempt_status',
            field=models.CharField(choices=[(4, 'attempted'), (6, 'disqualified'), (5, 'not-attempted')], default=5, max_length=2),
        ),
    ]
