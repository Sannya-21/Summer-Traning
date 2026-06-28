from django.db import models

class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('Electricity', 'Electricity'),
        ('Water', 'Water'),
        ('Cleaning', 'Cleaning'),
        ('Furniture', 'Furniture'),
        ('Internet', 'Internet'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    student_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='complaints/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name