# Generated by Django 4.1 on 2023-10-31 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer_Table',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('answer_text', models.TextField()),
                ('answered_by_user_id', models.IntegerField()),
                ('answered_by_user_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question_Table',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.TextField()),
                ('asked_by_user_id', models.IntegerField()),
                ('asked_by_user_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Like_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_by_user_id', models.IntegerField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts_app.answer_table')),
            ],
        ),
        migrations.AddField(
            model_name='answer_table',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts_app.question_table'),
        ),
    ]