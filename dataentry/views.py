from typing import List

from django.apps import apps
from django.shortcuts import render


def list_all_models() -> List[str]:
    excluded_models = [
        "User",
        "LogEntry",
        "Permission",
        "Group",
        "ContentType",
        "Session",
    ]
    _models = []
    for app in apps.get_app_configs():
        for model in app.get_models():
            if model.__name__ in excluded_models:
                continue
            _models.append(model.__name__)
    return _models


def import_data(request):
    context = {"all_models": list_all_models()}
    return render(request, "dataentry/importdata.html", context=context)
