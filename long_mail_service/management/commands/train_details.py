import json

from django.core.management import BaseCommand
from long_mail_service.api import TrainAPI


class Command(BaseCommand):
    help = """
    This command is used to create train details:
    train id: int
    
    """

    def add_arguments(self, parser):
        parser.add_argument("--train-id", type=str, help="Id of train")

    def handle(self, *args, **options):
        details = TrainAPI.get_train_details(options["train_id"])
        details = json.dumps(details)
        return "Train details: " + details
