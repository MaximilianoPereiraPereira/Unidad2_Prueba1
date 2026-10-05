from django.db import models

# Create your models here.

class categoria(models.Model):
    nombre = models.CharField(max_length=88, unique= True)

    class meta:
        verbose_name_plural = 'categorias'
        ordering =["nombre"]

    def __str__(self):
        return self.nombre

class producto (models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(null=True)
    precio = models.PositiveBigIntegerField(default=0)
    stock = models.PositiveBigIntegerField()
    activo = models.BooleanField(default=False,null= True)
    creado = models.DateField(auto_now_add=True)
    codigo = models.CharField(max_length=20)

    class meta:
        verbose_name_plurar = 'productos'
        ordering = ["nombre"]
    def __str__(self):
            return f"{self.nombre} ${self.precio}"


class cliente (models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField(unique=True)

    class meta:
        verbose_name_plurar = 'clientes'
        ordering = ["nombre"]
    def __str__(self):
            return f"{self.nombre} ${self.email}"


#----------------------Foraneas--------------------------

class pedido(models.Model):
    fecha = models.DateField()
    pagado = models.BooleanField()
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, related_name="cliente")
    
    class meta:
        verbose_name_plurar = "Pedidos"
        ordering =["fecha"]

    def __str__(self):
         return f"{self.id}:{self.fecha}"
