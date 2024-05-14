from django.core.management.base import BaseCommand

from dataentry.models import Student


class Command(BaseCommand):
    help = "Inserts data into the database"

    def handle(self, *args, **kwargs):

        Student.objects.create(name="Pedro", roll_no="1001", age=28)

        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))
