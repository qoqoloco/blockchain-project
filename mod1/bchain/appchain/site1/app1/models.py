from django.db import models
import faker
# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.name
        return self.email
        return self.phone

fk = faker.Faker()



# def popu(N=2):
#
#     for i in range(N):
#         a=fk.name()
#         b=fk.email()
#         c=fk.numerify()
#         z=Users.objects.get_or_create(name=a,email=b,phone=c)
#         # Users.objects.get_or_create(b)
#         # Users.objects.get_or_create(c)
#
# popu(3)
