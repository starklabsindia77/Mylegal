# Generated by Django 3.0.3 on 2020-05-07 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IPC_NUMBER', models.CharField(max_length=60)),
                ('DESCRIPTION', models.TextField()),
                ('IMAGE', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('STATUS', models.BooleanField(default=True)),
                ('CREATED_AT', models.DateTimeField(auto_now_add=True)),
                ('CATEGORY_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.Category')),
            ],
            options={
                'unique_together': {('IPC_NUMBER',)},
            },
        ),
    ]
