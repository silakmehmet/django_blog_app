from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):

    STATUS = (
        (1, "Published"),
        (2, "Draft")
    )

    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    status = models.SmallIntegerField(choices=STATUS, default=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
