# Generated by Django 4.0.3 on 2022-04-04 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_participant_meetup_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='test', max_length=254),
            preserve_default=False,
        ),
    ]
