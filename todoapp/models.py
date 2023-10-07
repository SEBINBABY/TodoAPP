from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TODO(models.Model):
    title = models.CharField(max_length=100)
    status_choices = [
        ("COMPLETED","COMPLETED"),
        ("PENDING","PENDING")
    ]
    priority_choices = [
        ("1","1️⃣"),
        ("2","2️⃣"),
        ("3","3️⃣"),
        ("4","4️⃣"),
        ("5","5️⃣"),
        ("6","6️⃣"),
        ("7","7️⃣"),
        ("8","8️⃣"),
        ("9","9️⃣"),
        ("10","🔟")

    ]
    status = models.CharField(max_length = 15,choices = status_choices )
    priority = models.CharField(max_length = 2,choices = priority_choices)
    date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)

