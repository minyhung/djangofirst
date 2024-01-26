from django.db import models

#apiapp_book 이라는 테이블을 생성
# Create your models here.
class Book(models.Model):
	bid = models.IntegerField(primary_key=True)
	title=models.CharField(max_length=50)
	author=models.CharField(max_length=50)
	publisheddate=models.DateField()


