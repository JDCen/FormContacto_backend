from django.db  import models
##from django.db  import contact


class Form(models.Model):
    id                  = models.AutoField(primary_key=True)
    gender_choices      = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]
    sexo = models.CharField(max_length=1, choices=gender_choices, verbose_name="Sexo")
    fecha_nacimiento   = models.DateField(verbose_name="Fecha de nacimiento")
    nombre              = models.CharField(max_length=100, verbose_name="Nombre")
    apellido            = models.CharField(max_length=100, verbose_name="Apellido")
    email               = models.EmailField(max_length=255, verbose_name="Email")
    direccion           = models.CharField(max_length=255, verbose_name="Dirección")
    casa_apto           = models.CharField(max_length=100, null=True, blank=True, verbose_name="Casa/Apartamento")
    pais_choices        = [
        ('CO', 'Colombia'),
        ('VE', 'Venezuela')
    ]
    pais            = models.CharField(max_length=30, choices=pais_choices, verbose_name="País")
    departamento_choices = [
            ('Bogotá D.C.', 'Bogotá D.C.'),
            ('Amazonas', 'Amazonas'),
            ('Antioquia', 'Antioquia'),
            ('Arauca', 'Arauca'),
            ('Atlántico', 'Atlántico'),
            ('Bolívar', 'Bolívar'),
            ('Boyacá', 'Boyacá'),
            ('Caldas', 'Caldas'),
            ('Caquetá', 'Caquetá'),
            ('Casanare', 'Casanare'),
            ('Cauca', 'Cauca'),
            ('Cesar', 'Cesar'),
            ('Chocó', 'Chocó'),
            ('Córdoba', 'Córdoba'),
            ('Cundinamarca', 'Cundinamarca'),
            ('Guainía', 'Guainía'),
            ('Guaviare', 'Guaviare'),
            ('Huila', 'Huila'),
            ('La Guajira', 'La Guajira'),
            ('Magdalena', 'Magdalena'),
            ('Meta', 'Meta'),
            ('Nariño', 'Nariño'),
            ('Norte de Santander', 'Norte de Santander'),
            ('Putumayo', 'Putumayo'),
            ('Quindío', 'Quindío'),
            ('Risaralda', 'Risaralda'),
            ('San Andrés y Providencia', 'San Andrés y Providencia'),
            ('Santander', 'Santander'),
            ('Sucre', 'Sucre'),
            ('Tolima', 'Tolima'),
            ('Valle del Cauca', 'Valle del Cauca'),
            ('Vaupés', 'Vaupés'),
            ('Vichada', 'Vichada'),]

    venezuela_estado_choices = [
            ('Amazonas', 'Amazonas'),
            ('Anzoátegui', 'Anzoátegui'),
            ('Apure', 'Apure'),
            ('Aragua', 'Aragua'),
            ('Barinas', 'Barinas'),
            ('Bolívar', 'Bolívar'),
            ('Carabobo', 'Carabobo'),
            ('Cojedes', 'Cojedes'),
            ('Delta Amacuro', 'Delta Amacuro'),
            ('Falcón', 'Falcón'),
            ('Guárico', 'Guárico'),
            ('Lara', 'Lara'),
            ('Mérida', 'Mérida'),
            ('Miranda', 'Miranda'),
            ('Monagas', 'Monagas'),
            ('Nueva Esparta', 'Nueva Esparta'),
            ('Portuguesa', 'Portuguesa'),
            ('Sucre', 'Sucre'),
            ('Táchira', 'Táchira'),
            ('Trujillo', 'Trujillo'),
            ('Vargas', 'Vargas'),
            ('Yaracuy', 'Yaracuy'),]
    departamento        = models.CharField(max_length=50, choices=departamento_choices + venezuela_estado_choices, verbose_name="Departamento")    
    ciudad              = models.CharField(max_length=50, verbose_name="Ciudad")
    descripcion         = models.CharField(max_length=100, verbose_name="Descripción", default='')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")