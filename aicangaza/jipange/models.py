from django.db import models

# two models one for the members and one one for the contributions

class Member(models.Model):
    name = models.CharField(max_length=100)
    number=models.CharField(max_length=100, null=True)
    contact= models.CharField(max_length=100, null=True)
    mtaa=models.CharField(max_length=100, null= True)
    def __str__(self):
        return self.name
    
    @property
    def contribution_list(self):
        return self.contributions_list.all()
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    target = models.IntegerField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contribution(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    member = models.ForeignKey(Member,  related_name='contributions_list', on_delete= models.CASCADE)
    event = models.ForeignKey(Event, related_name='contributions_list', on_delete= models.CASCADE, default=1)
    def __str__(self):
        return f"{self.amount} - {self.member.name} on {self.date}"      


    