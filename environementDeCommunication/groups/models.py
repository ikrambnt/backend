from django.db import models
from accounts.models import User

# Create your models here.

#1 ISIL RANIA MAROUA/IKRAM

#groups.objets.all() == select * from groups
#ISIL 

class Group(models.Model):
    #id caché par défaut
    name = models.CharField(max_length=255)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_groups')
    participants = models.ManyToManyField(User, related_name='participant_groups')

    class Meta:
        unique_together = ('id', 'admin')
    
    def __str__(self):
        return self.name + " " + str(self.admin) + " " + str(self.participants.all())
    


