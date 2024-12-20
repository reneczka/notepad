# Generated by Django 4.1.5 on 2023-06-12 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notepad_app', '0004_team_teammember_team_members_team_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notepad_app.team'),
        ),
        migrations.AddField(
            model_name='todolist',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notepad_app.team'),
        ),
    ]
