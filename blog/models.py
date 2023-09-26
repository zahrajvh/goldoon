from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.

class blog(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    description = models.CharField (_("توضیحات"), max_length=100)
    context = models.TextField("متن")
    image = models.ImageField(_("تصویر"), upload_to="blogs/", blank= True, null= True)
    created_at = models.DateTimeField(_("زمان انتشار"), default=timezone.now)
    author = models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.CASCADE, blank=True, null= True)

    category = models.ForeignKey("category", verbose_name=_("دسته بندی"), on_delete=models.CASCADE, related_name = "blog", blank=True, null= True)

    def __str__(self):
        return self.title

class category(models.Model):
    title = models.CharField(_("عنوان"),max_length=20)
    slug = models.SlugField(_("عنوان لاتین"),max_length=30)
    published_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    