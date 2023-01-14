from django.contrib import admin
from . import models


class ImportanceItem(admin.StackedInline):
    model = models.Item
    fk_name = 'importance_id'
    exclude = ('geography_id', 'skill_id')


class GeographyItem(admin.StackedInline):
    model = models.Item
    fk_name = 'geography_id'
    exclude = ('importance_id', 'skill_id')


class SkillItem(admin.StackedInline):
    model = models.Item
    fk_name = 'skill_id'
    exclude = ('importance_id', 'geography_id')


@admin.register(models.Importance)
class ImportanceAdmin(admin.ModelAdmin):
    inlines = [ImportanceItem, ]


@admin.register(models.Geography)
class GeographyAdmin(admin.ModelAdmin):
    inlines = [GeographyItem, ]


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    inlines = [SkillItem, ]


@admin.register(models.Profession)
class ProfessionAdmin(admin.ModelAdmin):
    pass
