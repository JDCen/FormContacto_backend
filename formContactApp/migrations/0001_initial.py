# Generated by Django 4.2.1 on 2023-05-11 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1, verbose_name='Sexo')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('casa_apto', models.CharField(blank=True, max_length=100, null=True, verbose_name='Casa/Apartamento')),
                ('pais', models.CharField(choices=[('CO', 'Colombia'), ('VE', 'Venezuela')], max_length=30, verbose_name='País')),
                ('departamento', models.CharField(choices=[('Bogotá D.C.', 'Bogotá D.C.'), ('Amazonas', 'Amazonas'), ('Antioquia', 'Antioquia'), ('Arauca', 'Arauca'), ('Atlántico', 'Atlántico'), ('Bolívar', 'Bolívar'), ('Boyacá', 'Boyacá'), ('Caldas', 'Caldas'), ('Caquetá', 'Caquetá'), ('Casanare', 'Casanare'), ('Cauca', 'Cauca'), ('Cesar', 'Cesar'), ('Chocó', 'Chocó'), ('Córdoba', 'Córdoba'), ('Cundinamarca', 'Cundinamarca'), ('Guainía', 'Guainía'), ('Guaviare', 'Guaviare'), ('Huila', 'Huila'), ('La Guajira', 'La Guajira'), ('Magdalena', 'Magdalena'), ('Meta', 'Meta'), ('Nariño', 'Nariño'), ('Norte de Santander', 'Norte de Santander'), ('Putumayo', 'Putumayo'), ('Quindío', 'Quindío'), ('Risaralda', 'Risaralda'), ('San Andrés y Providencia', 'San Andrés y Providencia'), ('Santander', 'Santander'), ('Sucre', 'Sucre'), ('Tolima', 'Tolima'), ('Valle del Cauca', 'Valle del Cauca'), ('Vaupés', 'Vaupés'), ('Vichada', 'Vichada'), ('Amazonas', 'Amazonas'), ('Anzoátegui', 'Anzoátegui'), ('Apure', 'Apure'), ('Aragua', 'Aragua'), ('Barinas', 'Barinas'), ('Bolívar', 'Bolívar'), ('Carabobo', 'Carabobo'), ('Cojedes', 'Cojedes'), ('Delta Amacuro', 'Delta Amacuro'), ('Falcón', 'Falcón'), ('Guárico', 'Guárico'), ('Lara', 'Lara'), ('Mérida', 'Mérida'), ('Miranda', 'Miranda'), ('Monagas', 'Monagas'), ('Nueva Esparta', 'Nueva Esparta'), ('Portuguesa', 'Portuguesa'), ('Sucre', 'Sucre'), ('Táchira', 'Táchira'), ('Trujillo', 'Trujillo'), ('Vargas', 'Vargas'), ('Yaracuy', 'Yaracuy')], max_length=50, verbose_name='Departamento')),
                ('ciudad', models.CharField(max_length=50, verbose_name='Ciudad')),
                ('descripcion', models.CharField(default='', max_length=100, verbose_name='Descripción')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
        ),
    ]