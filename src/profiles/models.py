from __future__ import unicode_literals

from django.utils import timezone

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
import uuid
from django.db import models
from django.conf import settings


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)
    firebase_chat_id = models.TextField("Firebase chat id", default=None, null=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)


class EventConnection(models.Model):
    from_user = models.ForeignKey(Profile, related_name='connection_requests_sent')
    to_user = models.ForeignKey(Profile, related_name='connection_requests_received')
    event_id = models.CharField(_('event_id'), blank=True, max_length=100)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _('Event Connection')
        unique_together = ('from_user', 'to_user')