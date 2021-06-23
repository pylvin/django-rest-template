from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models
from pytz import unicode


class SocialMedia(models.Model):
    media_types = (
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('youtube', 'YouTube')
    )
    media = models.CharField(choices=media_types, max_length=55, unique=True)
    url = models.URLField(_("Link"))

    class Meta:
        verbose_name = _("Social Media")
        verbose_name_plural = _("Social Media")

    def __str__(self):
        return unicode(f'{self.media}')


class Logo(models.Model):
    image = models.ImageField(upload_to='logo/images/')

    class Meta:
        verbose_name = _("Loqo")
        verbose_name_plural = _("Loqo")

    def save(self, *args, **kwargs):
        if self.pk is None and Logo.objects.exists():
            # self.pk is None :returns True within a new Model object, unless the object has a UUIDField as its primary_key.
            # self pk is not None: Object has a primary key i.e exist
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one Logo instance')
        return super(Logo, self).save(*args, **kwargs)

    def __str__(self):
        return unicode(f'{self.id}')


class Contact(models.Model):
    phone = models.CharField(_("Əlaqə Nömrəsi"), max_length=55)
    email = models.EmailField(_("E-poçt"))
    location = models.CharField(_("Adres"), max_length=100)

    class Meta:
        verbose_name = _("Əlaqə")
        verbose_name_plural = _("Əlaqə")

    def save(self, *args, **kwargs):
        if self.pk is None and Contact.objects.exists():
            # self.pk is None :returns True within a new Model object, unless the object has a UUIDField as its primary_key.
            # self pk is not None: Object has a primary key i.e exist
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one Contact instance')
        return super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return unicode(f'{self.id}')


class About(models.Model):
    content = RichTextField(_("Mətn"))

    class Meta:
        verbose_name = _("Haqqımızda")
        verbose_name_plural = _("Haqqımızda")

    def save(self, *args, **kwargs):
        if self.pk is None and About.objects.exists():
            # self.pk is None :returns True within a new Model object, unless the object has a UUIDField as its primary_key.
            # self pk is not None: Object has a primary key i.e exist
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one About instance')
        return super(About, self).save(*args, **kwargs)

    def __str__(self):
        return unicode(f'{self.id}')


class FAQ(models.Model):
    question = RichTextField(_("Sual"))
    answer = RichTextField(_("Cavab"))

    class Meta:
        verbose_name = _("Tez-tez verilən suallar")
        verbose_name_plural = _("Tez-tez verilən suallar")

    def __str__(self):
        return unicode(f'{self.id}')
