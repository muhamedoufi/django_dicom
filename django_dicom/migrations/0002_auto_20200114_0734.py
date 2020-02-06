# Generated by Django 2.2.8 on 2020-01-14 07:34

from django.db import migrations, models
import django_dicom.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_dicom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='scanning_sequence',
            field=django_dicom.models.fields.ChoiceArrayField(base_field=models.CharField(choices=[('SE', 'Spin Echo'), ('IR', 'Inversion Recovery'), ('GR', 'Gradient Recalled'), ('EP', 'Echo Planar'), ('RM', 'Research Mode')], max_length=2), blank=True, help_text='Description of the type of data taken', null=True, size=5),
        ),
        migrations.AlterField(
            model_name='series',
            name='sequence_variant',
            field=django_dicom.models.fields.ChoiceArrayField(base_field=models.CharField(choices=[('SK', 'Segmented k-Space'), ('MTC', 'Magnetization Transfer Contrast'), ('SS', 'Steady State'), ('TRSS', 'Time Reversed Steady State'), ('SP', 'Spoiled'), ('MP', 'MAG Prepared'), ('OSP', 'Oversampling Phase'), ('NONE', 'None')], max_length=4), blank=True, help_text='Variant of the scanning sequence', null=True, size=6),
        ),
    ]
