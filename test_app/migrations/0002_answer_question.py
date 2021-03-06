# Generated by Django 3.1.6 on 2021-02-08 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import test_app.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1024, verbose_name='Question')),
                ('image', models.ImageField(blank=True, upload_to=test_app.utilities.get_timestamp_path, verbose_name='Image')),
                ('single_answer', models.BooleanField(default=True, verbose_name='Is single answer?')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Question is active?')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1024, verbose_name='Answer')),
                ('image', models.ImageField(blank=True, upload_to=test_app.utilities.get_timestamp_path, verbose_name='Image')),
                ('correct', models.BooleanField(default=False, verbose_name='Correct ansver')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Answer is active?')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='test_app.question', verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'ordering': ['question', '-correct', '-created'],
            },
        ),
    ]
