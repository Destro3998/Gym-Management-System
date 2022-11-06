# Generated by Django 4.1.2 on 2022-10-27 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(max_length=500)),
                ('account_payments', models.CharField(max_length=500)),
                ('account_features_and_benefits', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity_name', models.CharField(max_length=500)),
                ('amenity_usage_info', models.CharField(max_length=500)),
                ('amenity_availability', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym_name', models.CharField(max_length=500)),
                ('gym_hours', models.CharField(max_length=500)),
                ('amenity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.amenity')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=500)),
                ('staff_email', models.EmailField(max_length=254, unique=True)),
                ('staff_address', models.CharField(max_length=500)),
                ('staff_roles', models.CharField(blank=True, choices=[('Cleaner', 'Cleaner'), ('Receptionist', 'Receptionist'), ('Instructor', 'Instructor')], max_length=50)),
                ('staff_hours', models.CharField(max_length=500)),
                ('staff_classes', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_plan', models.CharField(max_length=500)),
                ('membership_info', models.CharField(max_length=500)),
                ('membership_price', models.CharField(max_length=500)),
                ('membership_deal_info', models.CharField(max_length=500)),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.gym')),
            ],
        ),
        migrations.AddField(
            model_name='gym',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.staff'),
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=500)),
                ('equipment_usage_info', models.CharField(max_length=500)),
                ('equipment_availability', models.CharField(max_length=500)),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.gym')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=500)),
                ('class_timeslot', models.CharField(max_length=500)),
                ('class_availability', models.CharField(max_length=100)),
                ('class_staffinstructor', models.CharField(max_length=500)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.staff')),
            ],
        ),
    ]
