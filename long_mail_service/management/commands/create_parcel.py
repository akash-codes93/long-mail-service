from django.core.management import BaseCommand
from long_mail_service.api import ParcelAPI


class Command(BaseCommand):
    help = """
    This command is used to create parcel. Following parameters are required:
    volume: int
    weight: int
    """

    def add_arguments(self, parser):
        parser.add_argument("--volume", type=int, help="Total volume of that train can carry")
        parser.add_argument("--weight", type=int, help="Total weight of that train can carry")

    def handle(self, *args, **options):
        parcel_id =  ParcelAPI.create_parcel(options["volume"], options["weight"])
        return "Parcel created with details: " + str(parcel_id)