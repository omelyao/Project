from django.shortcuts import render
from . import models
from . import utils


def index(request):
    context = {}
    try:
        context['profession'] = models.Profession.objects.get(id=1)
    except Exception as e:
        pass
    return render(request, 'profession.html', context=context)


def importance(request):
    try:
        object = models.Importance.objects.get(id=1)
    except Exception as e:
        return render(request, 'detail.html')

    items = models.Item.objects.filter(importance_id=object.id).all()
    data = utils.get_context(items)
    return render(request, 'detail.html', context={'data': data})


def geography(request):
    try:
        object = models.Geography.objects.get(id=1)
    except Exception as e:
        return render(request, 'detail.html')

    items = models.Item.objects.filter(geography_id=object.id).all()
    data = utils.get_context(items)
    return render(request, 'detail.html', context={'data': data})


def skills(request):
    try:
        object = models.Skill.objects.get(id=1)
    except Exception as e:
        return render(request, 'detail.html')

    items = models.Item.objects.filter(skill_id=object.id).all()
    data = utils.get_context(items)
    return render(request, 'detail.html', context={'data': data})


def last_vacancies(request):
    context = {}

    try:
        context['items'] = utils.parser(models.Profession.objects.get(id=1).title)

    except Exception as e:
        pass
    return render(request, 'vacancies.html', context=context)