from django.db import models
from django.utils import timezone
from django.conf import settings

# class Area(models.Model):
#     options2 = (
#         ('North London', 'North London'),
#         ('West London', 'West London'),
#         ('South London', 'South London'),
#         ('East London', 'East London')
#     )
#     name = models.CharField(choices=options2, max_length=50)

#     def __str__(self):
#         return self.name


class Post(models.Model):

    options = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    )
    options2 = (
        ('North London', 'North London'),
        ('West London', 'West London'),
        ('South London', 'South London'),
        ('East London', 'East London')
    )
    area = models.CharField(choices=options2, max_length=50)
    difficulty = models.CharField(max_length=50, choices=options, default='Beginner')
    time = models.CharField(max_length=5)
    players_needed = models.IntegerField(max_length=1)
    description = models.TextField(unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    player = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sesh_post'
    )

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.time

