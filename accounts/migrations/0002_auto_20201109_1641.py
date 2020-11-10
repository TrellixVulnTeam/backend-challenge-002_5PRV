# Generated by Django 3.0.3 on 2020-11-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(null=True, verbose_name='date of birth'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='other', max_length=8, verbose_name='gender'),
        ),
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.CharField(help_text='in metres', max_length=255, null=True, verbose_name='height'),
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.CharField(help_text='in kgs', max_length=255, null=True, verbose_name='weight'),
        ),
    ]