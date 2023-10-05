from django.db import models
import datetime

# Create your models here.
# Category Model
class Category(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_all_categories():
        return Category.objects.all()



# Customer Model
class Customer(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name = "customer"
        verbose_name_plural = "customers"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("customer_detail", kwargs={"pk": self.pk})

    # to save the data
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False



# Product Model
class Products(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey("Category", verbose_name="category", on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/products/')

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_product_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=catogory_id)
        else:
            return Products.get_all_products()


# Orders View
class Order(models.Model):

    product = models.ForeignKey("Products", verbose_name="product name", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", verbose_name="customer", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return f'{self.customer} {self.product}'

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')


