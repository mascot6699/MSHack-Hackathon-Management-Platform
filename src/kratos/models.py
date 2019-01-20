import uuid

from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from profiles.models import Profile

contact_regex = RegexValidator(regex=r'^[1-9]{1}[0-9]{9}$', message="Contact number format(10 digits): ex: 8050248326")

EMP_STATUS = (
    ('student', 'Student'),
    ('looking', 'Looking For Job'),
    ('employed', 'Employed'),
)

AMB_STATUS = (
    ('applied', 'Applied'),
    ('on_hold', 'On Hold'),
    ('selected', 'Selected'),
)


class AmbassadorInfo(models.Model):
    url_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Profile, related_name='amb_user', blank=True, null=True)
    email = models.EmailField(max_length=255, default=None, null=True, blank=True, verbose_name=_("email"))
    name = models.CharField(max_length=200)
    contact_number = models.CharField(validators=[contact_regex], max_length=17, blank=True, null=True)
    dob = models.DateField(null=False, blank=False)
    city = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    professional_status = models.CharField(choices=EMP_STATUS, default='student', max_length=100)
    technical_skills = models.CharField(max_length=500)
    other_skills = models.CharField(max_length=500)
    technology_of_interest = models.CharField(max_length=500)
    work_experience = models.CharField(max_length=500)
    project_undertaken = models.CharField(max_length=500)
    publications = models.CharField(max_length=500)
    achievements = models.CharField(max_length=500)
    hobbies = models.CharField(max_length=500)
    heard = models.CharField(max_length=500, verbose_name="Where Did You Hear About Ambassador Program")
    created_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(choices=AMB_STATUS, max_length=100, default='applied')

    class Meta:
        app_label = "kratos"

    def __str__(self):
        return self.name + " " + self.status


class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    start_time = models.DateField(null=False, blank=False)
    end_time = models.DateField(null=False, blank=False)

    class Meta:
        app_label = "kratos"

    def __str__(self):
        return str(self.event_id) + " " + self.name


TASK_TYPE = (
    ('manual', 'Manual'),
    ('monitored', 'Monitored')
)

class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_type = models.CharField(choices=TASK_TYPE, max_length=100, default='student')
    name = models.CharField(max_length=200)

    class Meta:
        app_label = "kratos"

    def __str__(self):
        return str(self.task_id)