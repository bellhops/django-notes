# -*- coding: utf-8 -*-
from notes.models import Note
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline


class NoteInline(GenericTabularInline):
    model = Note

admin.site.register(Note)
