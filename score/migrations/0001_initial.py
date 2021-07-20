# Generated by Django 3.2.3 on 2021-07-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.IntegerField(default=None, null=True, verbose_name='学生号码')),
                ('name', models.CharField(max_length=32, verbose_name='学生姓名')),
                ('score', models.IntegerField(verbose_name='学生分数')),
            ],
            options={
                'verbose_name': '分数表',
                'db_table': 'score',
            },
        ),
    ]
