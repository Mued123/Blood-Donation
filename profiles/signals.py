from django.db.models.signals import post_save,pre_delete
from accounts.models import User
from django.dispatch import receiver
from .models import Aprofile


@receiver(post_save,sender =User)
def post_save_create_profile(sender,instance,created,**kwargs):
    
    if created:
        Aprofile.objects.create(user = instance)