# Generated by Django 4.0.5 on 2022-06-15 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Type',
            new_name='Product_type',
        ),
        migrations.RemoveField(
            model_name='bio',
            name='Bio_author',
        ),
        migrations.AddField(
            model_name='addresse',
            name='Address_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='home.person'),
        ),
        migrations.AddField(
            model_name='bio',
            name='Author',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.person'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.person'),
        ),
    ]
