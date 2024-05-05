from django.db import models

# Create your models here.

class User(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=200)
    telefono_personal = models.CharField(max_length=15)
    correo_electronico = models.EmailField(unique=True)
    TIPO_CHOICES = (
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    )
    tipo_usuario = models.CharField(max_length=12, choices=TIPO_CHOICES)

class Property(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    cantidad_estacionamientos = models.PositiveIntegerField()
    cantidad_habitaciones = models.PositiveIntegerField()
    cantidad_banos = models.PositiveIntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=100)
    TIPO_INMUEBLE_CHOICES = (
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('parcela', 'Parcela'),
    )
    tipo_inmueble = models.CharField(max_length=12, choices=TIPO_INMUEBLE_CHOICES)
    precio_arriendo_mensual = models.DecimalField(max_digits=10, decimal_places=2)






# Crear un usuario
usuario = User.objects.create(
    nombres='Juan',
    apellidos='Perez',
    rut='12345678-9',
    direccion='Calle 123',
    telefono_personal='123456789',
    correo_electronico='juan@example.com',
    tipo_usuario='arrendatario'
)

# Crear una propiedad
propiedad = Property.objects.create(
    nombre='Casa en Condominio',
    descripcion='Hermosa casa en condominio cerrado',
    m2_construidos=150.5,
    m2_totales=200,
    cantidad_estacionamientos=2,
    cantidad_habitaciones=3,
    cantidad_banos=2,
    direccion='Calle Los Sauces 123',
    comuna='Santiago',
    tipo_inmueble='casa',
    precio_arriendo_mensual=1000000
)


# Listar todos los usuarios
todos_los_usuarios = User.objects.all()

# Listar usuarios de un tipo específico
usuarios_arrendatarios = User.objects.filter(tipo_usuario='arrendatario')

# Recuperar el usuario que queremos actualizar
usuario_a_actualizar = User.objects.get(rut='12345678-9')

# Actualizar los datos del usuario
usuario_a_actualizar.telefono_personal = '987654321'
usuario_a_actualizar.save()

# Recuperar el usuario que queremos eliminar
usuario_a_eliminar = User.objects.get(rut='12345678-9')

# Eliminar el usuario
usuario_a_eliminar.delete()