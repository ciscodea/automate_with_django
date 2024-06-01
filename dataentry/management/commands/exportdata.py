import csv
import datetime

from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Export data from databaset to a CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "model_name",
            type=str,
            help="Name of the model to export data from",
        )

    def handle(self, *args, **kwargs):

        model_name = kwargs["model_name"]
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = app_config.get_model(model_name)
                break
            except LookupError:
                continue

        if not model:
            self.stderr.write(f"Model [{model_name}] not found")
            return

        data = model.objects.all()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        file_path = f"exported_{model_name}_data_{timestamp}.csv"

        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)

            # write the csv header.
            headers = [field.name for field in model._meta.fields]
            writer.writerow(headers)

            # write data rows
            for dt in data:
                writer.writerow(
                    [getattr(dt, field.name) for field in model._meta.fields]
                )

        self.stdout.write(self.style.SUCCESS("Data exported successfully"))
