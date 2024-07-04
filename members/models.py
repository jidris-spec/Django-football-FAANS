
from datetime import timezone
from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    joined_date = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

# member = Member(
#     firstname='Idris',
#     lastname='Adedamola',
#     joined_date=timezone.now()  # Assuming you have a field `joined_date`
# )
# member.save()


# from django.db import models
# from django.utils import timezone

# class Member(models.Model):
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     joined_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.firstname} {self.lastname}"
