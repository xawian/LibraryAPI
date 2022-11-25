from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=35)
    unique_number = models.PositiveIntegerField(unique=True, auto_created=True)

    def __str__(self):
        return self.surname

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Release(models.Model):
    release_year = models.DateField()
    release_place = models.CharField(max_length=30)

    def __str__(self):
        return self.release_place


class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=35)
    country = models.CharField(max_length=35)
    birth_date = models.DateField()

    def __str__(self):
        return self.surname


class Status(models.Model):
    hired = models.BooleanField(default=False)
    hire_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return str(self.hired)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    release = models.OneToOneField(Release, on_delete=models.CASCADE)
    status = models.OneToOneField(Status, on_delete=models.CASCADE, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=35)
    login = models.CharField(max_length=30,null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    debt = models.FloatField(default=0)

    def __str__(self):
        return self.surname


class Hire(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    hire_date = models.DateField(null=True)



class Return(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    return_date = models.DateField()


class Assesment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    assesment = models.PositiveIntegerField()



