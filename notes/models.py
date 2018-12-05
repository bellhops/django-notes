# -*- coding: utf-8 -*-

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):

    created = models.DateTimeField(_('created'), default=now, editable=False, blank=True)
    modified = models.DateTimeField(_('modified'), default=now, editable=False, blank=True)

    class Meta:
        abstract = True
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)

    def save(self, *args, **kwargs):
        self.modified = now()
        if 'update_fields' in kwargs:
            kwargs['update_fields'] += ('modified',)
        super(TimeStampedModel, self).save(*args, **kwargs)


class Note(TimeStampedModel):
    """
    A simple model to handle adding arbitrary numbers of notes to a generic object.
    """
    content = models.TextField(_('Content'))
    public = models.BooleanField(_('Public'), default=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    objects = models.Manager()

    class Meta:
        verbose_name = _('Note')
        verbose_name_plural = _('Notes')

    @models.permalink
    def get_absolute_url(self):
        return ('notes-view', (), {'pk': self.pk})
