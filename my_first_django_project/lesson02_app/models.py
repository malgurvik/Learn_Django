from django.db import models
from django.template.defaulttags import lorem


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    biography = models.TextField()
    birth_date = models.DateField()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    registration_date = models.DateField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    amount = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)


class Order(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

