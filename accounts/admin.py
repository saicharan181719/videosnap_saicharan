from accounts.models import CareerBreak
from accounts.models import Language
from accounts.models import Service
from accounts.models import Position
from accounts.models import Certification
from accounts.models import Experience
from accounts.models import Skill
from accounts.models import Education
import accounts
from django.contrib import admin
from .models import *
admin .site.register(Education)
admin .site.register(Profile)
admin .site.register(Experience)
admin .site.register(Skill)
admin .site.register(Project)
admin .site.register(Certification)
admin .site.register(Position)
admin .site.register(Service)
admin .site.register(Language)
admin .site.register(CareerBreak)
