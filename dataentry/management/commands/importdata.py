import csv

from django.apps import apps
from django.core.management.base import BaseCommand, CommandError, CommandParser

from dataentry.models import Student


class Command(BaseCommand):
    help = "Inserts data from CSV file into the database"

    def add_arguments(self, parser: CommandParser):
        parser.add_argument("file_path", type=str, help="Path to the CSV file")
        parser.add_argument("model_name", type=str, help="Name of the model")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        model_name = kwargs["model_name"]

        # Search for the model in installed apps
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue

        if not model:
            raise CommandError(
                f"Model {model_name} not found or not in installed apps."
            )

        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))
