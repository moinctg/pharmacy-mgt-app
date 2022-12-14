# Generated by Django 3.2.6 on 2022-10-24 16:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='doctor/')),
                ('address', models.CharField(max_length=60)),
                ('contact', models.BigIntegerField()),
                ('speciality', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='StoreKipper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.BigIntegerField()),
                ('nid', models.CharField(max_length=50)),
                ('Salary', models.BigIntegerField()),
                ('join_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.BigIntegerField()),
                ('location', models.CharField(max_length=50)),
                ('store_kiper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.storekipper')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(blank=True, max_length=50, null=True)),
                ('drug_color', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('receive_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('manufacture', models.CharField(blank=True, max_length=50, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('valid_from', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('valid_to', models.DateTimeField(null=True)),
                ('drug_description', models.TextField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category/')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmacy.category')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=60)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('contact', models.BigIntegerField()),
                ('details', models.CharField(max_length=150)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.doctor')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.hospital'),
        ),
        migrations.CreateModel(
            name='Dispense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispense_quantity', models.PositiveIntegerField(default='1', null=True)),
                ('taken', models.CharField(blank=True, max_length=300, null=True)),
                ('stock_ref_no', models.CharField(blank=True, max_length=300, null=True)),
                ('instructions', models.TextField(max_length=300, null=True)),
                ('dispense_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('drug_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacy.stock')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_no', models.IntegerField(blank=True, db_index=True, null=True)),
                ('doc_dt', models.DateField(default=django.utils.timezone.now)),
                ('mode', models.CharField(choices=[('CASH', 'CASH'), ('CREDIT', 'CREDIT'), ('BANK', 'BANK')], default='CASH', max_length=10)),
                ('sale_discount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6)),
                ('sale_disc_type', models.CharField(choices=[('Rs', 'Rs'), ('Percent', '%')], default='Percent', max_length=10)),
                ('sale_adjustment', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('net_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('rec_amt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('net_cgst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8)),
                ('net_sgst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8)),
                ('net_gst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8)),
                ('due_amt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6)),
                ('use_date', models.DateField(blank=True, null=True)),
                ('ref_note', models.CharField(blank=True, max_length=50, null=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pharmacy.storekipper')),
            ],
            options={
                'unique_together': {('doc_no', 'doc_dt')},
            },
        ),
    ]
