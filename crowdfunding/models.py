from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Campaign(models.Model):
    owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name='campaigns')
    title = models.CharField(max_length=220)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Donation(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT, related_name='donatins')
    backer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.backer} donated {self.amount} to {self.campaign}'
    
    