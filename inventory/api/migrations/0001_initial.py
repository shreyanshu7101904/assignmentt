# Generated by Django 3.2.7 on 2021-09-13 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.basemodel')),
                ('name', models.CharField(db_index=True, max_length=64)),
            ],
            options={
                'db_table': 'supplier',
                'ordering': ['-created'],
            },
            bases=('api.basemodel',),
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.basemodel')),
                ('name', models.CharField(db_index=True, max_length=32)),
                ('description', models.CharField(max_length=256)),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
                ('stock', models.IntegerField(default=0)),
                ('availability', models.BooleanField(default=False)),
                ('supplied_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supplier', to='api.supplier')),
            ],
            options={
                'db_table': 'inventory',
                'ordering': ['-created'],
            },
            bases=('api.basemodel',),
        ),
    ]
