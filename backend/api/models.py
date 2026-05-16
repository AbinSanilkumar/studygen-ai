from django.db import models


class Note(models.Model):

    image = models.ImageField(upload_to='notes/')

    extracted_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note {self.id}"