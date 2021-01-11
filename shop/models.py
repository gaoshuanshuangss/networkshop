from django.db import models


# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=10)

    def __unicode__(self):
        return f"Category:{self.cname}"


class Goods(models.Model):
    gname = models.CharField(max_length=100)
    gdesc = models.CharField(max_length=100)
    oldprice = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return f"Goods:{self.gname}"


class GoodsDetailName(models.Model):
    gdname = models.CharField(max_length=30)

    def __unicode__(self):
        return f"GoodsDetailName:{self.gdname}"


class GoodsDetail(models.Model):
    gdurl = models.ImageField(upload_to="")
    gdname = models.ForeignKey(GoodsDetailName, blank=True, null=True, on_delete=models.SET_NULL)
    goods = models.ForeignKey(Goods, blank=True, null=True, on_delete=models.SET_NULL)


class Size(models.Model):
    sname = models.CharField(max_length=10)

    def __unicode__(self):
        return f"Size:{self.sname}"


class Color(models.Model):
    colorname = models.CharField(max_length=10)
    colorurl = models.ImageField(upload_to="color/")

    def __unicode__(self):
        return f"Color:{self.colorname}"


class Inventory(models.Model):
    count = models.PositiveIntegerField()
    color = models.ForeignKey(Color,blank=True, null=True,  on_delete=models.SET_NULL)
    goods = models.ForeignKey(Goods, blank=True, null=True, on_delete=models.SET_NULL)
    size = models.ForeignKey(Size,blank=True, null=True,  on_delete=models.SET_NULL)
