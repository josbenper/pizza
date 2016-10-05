from django.db import models

# Create your models here.
class Ingredients(models.Model):
	#idIngredients = models.CharField(max_length=35, editable = False)
	idIngredients = models.CharField(max_length=35)
	name = models.CharField(max_length=35)
	price = models.FloatField(null=False, blank=False)

	def save(self, *args, **kwargs):
		if not self.idIngredients:
			i = Ingredients.objects.all().order_by('-idIngredients')[0]
			self.idIngredients = i.idIngredients+1
		super(Ingredients, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

class Pizzas(models.Model):
	idPizza = models.CharField(max_length=35)
	name = models.CharField(max_length=35)
	ingredients = models.ManyToManyField('Ingredients', null=True)
	#image = models.FloatField(null=False, blank=False)
	image = models.ImageField(upload_to = 'pic_folder/', null=True)
	prices = models.FloatField(null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.idPizza:
			i = Pizzas.objects.all().order_by('-idPizza')[0]
			self.idPizza = int(i.idPizza)+1

		precio = 0

		for x in self.ingredients.all():
			print (x.price)
			precio = precio + x.price		
		
		precio = precio + precio / 2
		self.prices = precio
		super(Pizzas, self).save(*args, **kwargs)

	def __str__(self):
		return self.name