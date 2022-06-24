from django.db import models

class User(models.Model):
    # Limit username length
    username = models.CharField(max_length=20)
    # Allow long image urls
    photo = models.CharField(max_length=256)


class Bunk(models.Model):
    # Allow bunks sent by deleted users to remain
    from_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='bunks_sent')
    # Delete bunks given to deleted users
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bunks_received')
    # Automatically set bunk times for convenience
    time = models.DateTimeField(auto_now_add = True)
