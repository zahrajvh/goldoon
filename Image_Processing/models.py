from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class processing(models.Model):
    
    photo = models.ImageField(_("تصویر گل"), upload_to='process/')

