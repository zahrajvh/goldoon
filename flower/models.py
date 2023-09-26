from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class flower(models.Model):
    EN_name = models.CharField(max_length=70, default="unknown")
    name = models.CharField(max_length=50)
    description = models.TextField(_("توضیحات"), max_length=10000)
    care = models.TextField(_("شیوه نگهداری"), max_length=10000, default="")
    water_requirement = models.CharField(max_length=130, default="")
    suitable_weather = models.CharField(max_length=130, default="")
    photo = models.ImageField(upload_to='flower/')
    flower_type = [
        ("apartment", "آپارتمانی"),
        ("garden", "باغچه ای"),
        ("ornamental", "زینتی")
    ]
    type_flower = models.CharField(_("نوع گل"), choices = flower_type, default= "garden", max_length= 50)

    def __str__(self):
        return self.name