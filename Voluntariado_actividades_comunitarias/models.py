from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class PerfilVoluntario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_voluntario')
    telefono = models.CharField(max_length=20, blank=True, null=True)
    rut_o_dni = models.CharField(max_length=20, unique=True, blank=True, null=True)
    habilidades = models.TextField(blank=True, help_text="Ej: Primeros auxilios, carpintería, docencia...")
    disponibilidad = models.CharField(max_length=100, blank=True, help_text="Ej: Fines de semana, tardes...")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    habilitado = models.BooleanField(default=True)

    class Meta:
        db_table_comment = "Perfil de voluntarios con información adicional"

    def __str__(self):
        return f"Voluntario: {self.user.get_full_name() or self.user.username}"


class Organizacion(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField()
    contacto_email = models.EmailField()
    contacto_telefono = models.CharField(max_length=20, blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)
    encargado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='organizaciones_a_cargo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    habilitado = models.BooleanField(default=True)

    class Meta:
        db_table_comment = "Organizaciones que ofrecen actividades comunitarias"

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    habilitado = models.BooleanField(default=True)

    class Meta:
        db_table_comment = "Categorías de actividades comunitarias"

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    ESTADO_CHOICES = [
        ('borrador', 'Borrador'),
        ('publicada', 'Publicada'),
        ('en_progreso', 'En Progreso'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE, related_name='actividades')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='actividades')
    
    ubicacion = models.CharField(max_length=255, help_text="Dirección o punto de encuentro")
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    
    cupos_maximos = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='publicada')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    habilitado = models.BooleanField(default=True)

    class Meta:
        db_table_comment = "Actividades comunitarias ofrecidas por organizaciones"

    def __str__(self):
        return f"{self.titulo} - {self.organizacion.nombre}"

    @property
    def cupos_disponibles(self):
        inscritos = self.inscripciones.filter(estado__in=['pendiente', 'aceptada']).count()
        return max(0, self.cupos_maximos - inscritos)


class Inscripcion(models.Model):
    ESTADO_INSCRIPCION = [
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
        ('cancelada', 'Cancelada por el Voluntario'),
    ]

    voluntario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inscripciones')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name='inscripciones')
    estado = models.CharField(max_length=20, choices=ESTADO_INSCRIPCION, default='pendiente')
    asistio = models.BooleanField(default=False, help_text="Confirmación de asistencia tras realizar la actividad")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    habilitado = models.BooleanField(default=True)

    class Meta:
        db_table_comment = "Inscripciones de voluntarios a actividades"

    def __str__(self):
        return f"{self.voluntario.username} -> {self.actividad.titulo} ({self.estado})"


class Resena(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name='resenas')
    voluntario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resenas')
    calificacion = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Escala de 1 a 5"
    )
    comentario = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    habilitado = models.BooleanField(default=True)

    class Meta:
        db_table_comment = "Reseñas de actividades por voluntarios"

    def __str__(self):
        return f"Reseña de {self.voluntario.username} en {self.actividad.titulo} ({self.calificacion}/5)"


class Comuna(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    habilitado = models.BooleanField(default=True)

    class Meta:
        db_table_comment = "Catálogo de comunas y regiones para normalizar ubicaciones de actividades"

    def __str__(self):
        return f"{self.nombre} ({self.region})"


class Habilidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    habilitado = models.BooleanField(default=True)

    class Meta:
        db_table_comment = "Catálogo de habilidades que pueden tener los voluntarios"

    def __str__(self):
        return self.nombre


class HistorialEstadoInscripcion(models.Model):
    inscripcion = models.ForeignKey('Inscripcion', on_delete=models.CASCADE, related_name='historial')
    estado_anterior = models.CharField(max_length=20, blank=True, null=True)
    estado_nuevo = models.CharField(max_length=20)
    observacion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    habilitado = models.BooleanField(default=True)

    class Meta:
        db_table_comment = "Historial de cambios de estado de las inscripciones"

    def __str__(self):
        return f"Inscripción #{self.inscripcion.id}: {self.estado_anterior} -> {self.estado_nuevo}"