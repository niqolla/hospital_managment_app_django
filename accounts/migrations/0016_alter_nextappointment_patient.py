# Generated by Django 4.1 on 2023-03-01 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_rename_patient_patienthasallergy_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nextappointment',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_next_app', to='accounts.patient'),
        ),
    ]
