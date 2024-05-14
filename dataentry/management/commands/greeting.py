from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    help = "Greets the user"

    def add_arguments(self, parser: CommandParser):
        parser.add_argument("name", type=str, help="Specifies user name")

    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        self.stdout.write(f"Hi there {name}! Welcome to the data entry system.")
