from long_mail_service.models import Parcel
from long_mail_service.service.serializers import ParcelSerializer


class ParcelService:

    @staticmethod
    def create_parcel(volume: int, weight: int) -> int:
        """
        Create the parcel using volume and weight
        """
        parcel = Parcel.objects.create(volume=volume, weight=weight)
        parcel.save()

        return ParcelSerializer(parcel).data

    @staticmethod
    def get_parcel(parcel_id: id):
        """
        Get parcel using parcel_id
        """
        try:
            parcel = Parcel.objects.get(id=parcel_id)
            return ParcelSerializer(parcel).data
        except Parcel.DoesNotExist:
            return None

    @staticmethod
    def get_available_parcels():
        """
        Get list of all the available parcels in the system.
        """
        parcels = Parcel.objects.filter(booking__isnull=True)
        return ParcelSerializer(parcels, many=True).data


parcel_service = ParcelService()
