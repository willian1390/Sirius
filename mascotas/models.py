from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.



class Lugar(models.Model):
	id_lugar = models.AutoField(primary_key=True)
	nombre_lugar = models.CharField(max_length=50)
	calle = models.CharField(max_length=50)
	avenida = models.CharField(max_length=50)
	#no_casa = models.CharField(max_length=50, null=True, blank=True)
	zona = models.IntegerField()
	otra_especificacion = models.TextField(max_length=50, null=True, blank=True)

	class Meta:
		verbose_name = 'lugar'
		verbose_name_plural = 'lugares'

	def NombreDeLugar(self):
		cadena="{0}"
		return cadena.format(self.nombre_lugar)
			
	def __str__(self):
		return self.NombreDeLugar()


class Raza(models.Model):
	id_raza = models.AutoField(primary_key=True)
	nombre_raza = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=50)

	class Meta:
		verbose_name = 'raza'
		verbose_name_plural = 'razas'
			
	def __str__(self):
		return self.nombre_raza


class Vacuna(models.Model):
	id_vacuna = models.AutoField(primary_key=True)
	nombre_vacuna = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=100)
	precio = models.FloatField()

	class Meta:
		verbose_name = 'vacuna'
		verbose_name_plural = 'vacunas'
			
	def __str__(self):
		return self.nombre_vacuna


class Medicamento(models.Model):
	id_medicamento = models.AutoField(primary_key=True)
	nombre_medicamento = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=100)
	precio = models.FloatField()

	class Meta:
		verbose_name = 'medicamento'
		verbose_name_plural = 'medicamentos'
			
	def __str__(self):
		return self.nombre_medicamento



class Mascota(models.Model):
	id_mascota = models.AutoField(primary_key=True)
	fecha_recate = models.DateField(verbose_name="Fecha de Rescate")
	nombre_mascota = models.CharField(max_length=50, verbose_name="Nombre")
	edad_aprox = models.IntegerField(verbose_name="Edad")
	color = models.CharField(max_length=50)
	sexos = (('H','Hembra'),('M','Macho'))
	sexo = models.CharField(max_length=1, choices=sexos, default='M')
	sena_particular = models.CharField(max_length=200, blank=True)
	esteriliza = (('S','Si'),('N','No'))
	esterilizado = models.CharField(max_length=1, choices=esteriliza, default='N')
	imagen = models.ImageField(upload_to='mascotas')

	lugar_rescate=models.ForeignKey(Lugar, default=None, null=False,blank=False, on_delete=models.CASCADE)
	raza=models.ForeignKey(Raza, null=False, default=None, blank=False, on_delete=models.CASCADE)
	vacuna=models.ManyToManyField(Vacuna, blank=True)
	medicamento=models.ManyToManyField(Medicamento, blank=True)
	
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	#admin = models.ForeignKey(User, default=None, null=False,blank=False, on_delete=models.CASCADE)


	class Meta:
		verbose_name = 'mascota'
		verbose_name_plural = 'mascotas rescatadas'
			
	def NombreMascota(self):
		cadena="{0}"
		return cadena.format(self.nombre_mascota)
			
	def __str__(self):
		return self.NombreMascota()

	def Vacunas_(self):
		return " ,".join([str(p) for p in self.vacuna.all()])

	def Medicamentos_(self):
		return " ,".join([str(p) for p in self.medicamento.all()])


#ADOPCIONES DE MASCOTAS
class Adopcion(models.Model):
	id_adopcion=models.AutoField(primary_key=True)
	fecha_adopcion=models.DateTimeField(auto_now_add=True)
	admin = models.ForeignKey(User, default=None, null=False,blank=False, on_delete=models.CASCADE)
	mascota = models.ForeignKey(Mascota, null=False, blank=False,on_delete=models.CASCADE)

	nombres_adoptante=models.CharField(max_length=100)
	apellidos_adoptante=models.CharField(max_length=100)
	edad_adoptante = models.IntegerField(verbose_name="Edad")
	dpi_adoptante=models.CharField(max_length=50)
	direccion_adoptante=models.CharField(max_length=50)
	telefono_adoptante=models.CharField(max_length=50)
	redes_adoptante=models.CharField(max_length=50)

	pregunta1=models.TextField(verbose_name="¿Cuál es la razón por la que busca adoptar un perro?")
	pregunta2=models.TextField(verbose_name="¿Por qué le interesa esta mascota en específico?")
	pregunta3=models.CharField(max_length=100, verbose_name="¿Tiene otros animales actualmente en casa?")
	pregunta4=models.CharField(max_length=100, verbose_name="¿Está de acuerdo que se le visite periódicamente para dar seguimiento a la adopción, para ver el estado de salud y bienestar la mascota que desea adoptar?")
	pregunta5=models.CharField(max_length=100, verbose_name="¿Estaría de acuerdo en notificar a la Asociación si tuviera cambio de dirección?")
	pregunta6=models.CharField(max_length=100, verbose_name="¿Tiene espacio adecuado para la mascota?")
	pregunta8=models.CharField(max_length=100, verbose_name="¿Quién será responsable de cubrir los gastos veterinarios, limpiar, cuidar y alimentar a la mascota que desea adoptar?")
	pregunta9=models.CharField(max_length=100, verbose_name="¿Están de acuerdo todos los miembros de su familia en la adopción de una mascota?")
	pregunta10=models.CharField(max_length=100, verbose_name="¿Está de acuerdo en castrar (en caso de ser hembra) a la mascota que desea adoptar, para evitar la reproducción animal y pagar la misma?")
	pregunta11=models.CharField(max_length=100, verbose_name="¿Está consciente de que una mascota necesita alimentación adecuada, un lugar cómodo para descansar, vacunas anuales, gastos veterinarios, shampoos especiales y baños frecuentes?")
	pregunta12=models.CharField(max_length=100, verbose_name="¿Sabe usted que un cachorro es travieso por naturaleza, puede romper zapatos, ropa, juguetes que se dejen descuidados a su alcance?")
	pregunta13=models.CharField(max_length=100, verbose_name="¿Tiene usted el tiempo de entrenar a la mascota para que haga sus necesidades en algún lugar en específico?")
	pregunta14=models.CharField(max_length=100, verbose_name="¿Sabe usted que hay enfermedades graves transmitidas por las garrapatas?, por lo que es necesario mantener a las mascotas libres de estas plagas.")

	class Meta:
		verbose_name = 'adopción'
		verbose_name_plural = 'adoptar una Mascota'

#PUBLICACIONES DE MASCOTAS
class Adoptar_Mascota(models.Model):
	mascota = models.ForeignKey(Mascota, null=False, blank=False, on_delete=models.CASCADE)
	descripcion = RichTextField(verbose_name="Descripcion de mascota")
	iadoptar = models.ImageField(upload_to='adopcion')
	active = models.BooleanField(default=True, verbose_name="Publicado?")


	class Meta:
		verbose_name = 'Publicar Mascota'
		verbose_name_plural = 'Publicar Mascota - Adopcion'
