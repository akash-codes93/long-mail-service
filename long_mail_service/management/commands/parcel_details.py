import json

from django.core.management import BaseCommand
from long_mail_service.api import ParcelAPI


class Command(BaseCommand):
    help = """
    This command is used to create train details:
    train id: int
    """

    def add_arguments(self, parser):
        parser.add_argument("--parcel-id", type=str, help="Id of train")

    def handle(self, *args, **options):
        details = ParcelAPI.get_parcel_details(options["parcel_id"])
        details = json.dumps(details)
        return "Parcel details: " + details