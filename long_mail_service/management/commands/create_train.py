from django.core.management import BaseCommand
from long_mail_service.api import TrainAPI


class Command(BaseCommand):
    help = """
    This command is used to create train. Following parameters are required:
    name: str
    cost: int
    volume: int
    weight: int
    lines: List[int]
    """

    def add_arguments(self, parser):
        parser.add_argument("--name", type=str, help="Name of train")
        parser.add_argument("--cost", type=int, help="Cost of train per item")
        parser.add_argument("--volume", type=int, help="Total volume of that train can carry")
        parser.add_argument("--weight", type=int, help="Total weight of that train can carry")
        parser.add_argument("--lines", nargs="+", type=str, help="Line of train")

    def handle(self, *args, **options):
        train_id =  TrainAPI.create_train(options["name"], options["cost"], options["volume"], options["weight"],
                                     options["lines"])

        return "Train created with details: " + str(train_id)