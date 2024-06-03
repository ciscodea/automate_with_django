from typing import List

from django.apps import apps
from django.conf import settings
from django.contrib import messages
from django.core.management import call_command
from django.shortcuts import redirect, render

from uploads.models import Upload


def list_all_models() -> List[str]:
    excluded_models = [
        "User",
        "LogEntry",
        "Permission",
        "Group",
        "ContentType",
        "Session",
        "Upload"
    ]
    _models = []
    for app in apps.get_app_configs():
        for model in app.get_models():
            if model.__name__ in excluded_models:
                continue
            _models.append(model.__name__)
    return _models


def import_data(request):
    if request.method == "POST":
        file_path = request.FILES.get("file_path")
        model_name = request.POST.get("model_name")

        upload = Upload.objects.create(file=file_path, model_name=model_name)
        
        # Construct the full path of uploaded file
        relative_path = str(upload.file.url)
        base_url = str(settings.BASE_DIR)
        file_path = base_url + relative_path

        # Call command
        try:
            call_command("importdata", file_path, model_name)
            messages.success(request, "Data imported successfully!")
        except Exception as e:
            messages.error(request, str(e))

        return redirect("import_data")
    else:
        context = {"all_models": list_all_models()}
    return render(request, "dataentry/importdata.html", context=context)
