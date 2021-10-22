from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.birthday}'


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=120)
    date = models.IntegerField()

    def __str__(self):
        return f'{self.author.name} - {self.title} - {self.date}'


class CSV(models.Model):
    file_name = models.CharField(max_length=120, null=True)
    csv_file = models.FileField(upload_to='csvs', null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file_name)
