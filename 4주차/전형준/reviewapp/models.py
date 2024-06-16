from django.db import models
from bookapp.models import Book

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # created_at과 updated_at는 거의 필수
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews') # ForeignKey가 가리키는 book이 삭제되면 해당 review도 모두 삭제

    def __str__(self):
        return self.title