from django.core.management import BaseCommand
from long_mail_service.api import PostMasterAPI


class Command(BaseCommand):
    help = """
    This command is used to schedule parcel
    """

    def handle(self, *args, **options):
        parcel_id =  PostMasterAPI.schedule_parcel()
        return "Schedule: " + str(parcel_id)