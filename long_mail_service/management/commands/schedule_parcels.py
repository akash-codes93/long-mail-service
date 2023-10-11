from django.core.management import BaseCommand
from long_mail_service.api import PostMasterAPI


class Command(BaseCommand):
    help = """
    This command is used to schedule parcel
    """

    def add_arguments(self, parser):
        parser.add_argument("--strategy", type=str, help="Id of train")

    def handle(self, *args, **options):
        parcel_id =  PostMasterAPI.schedule_parcel(options["strategy"])
        return "Schedule: " + str(parcel_id)