# Generated by Django 4.0 on 2022-04-10 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_alter_재활센터_id_alter_지역_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='재활센터',
            old_name='싸이트',
            new_name='웹사이트',
        ),
        migrations.AlterField(
            model_name='재활센터',
            name='정보',
            field=models.TextField(max_length=1400),
        ),
    ]
