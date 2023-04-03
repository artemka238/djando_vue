from django.db import models

class Task(models.Model):
    title = models.CharField(max_length = 150)
    description = models.TextField(blank = True, null = True)
    complited = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self) -> str:
        return self.title
