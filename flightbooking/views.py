from asyncio import mixins
from rest_framework import viewsets
from .models import Booking, Flight
from .serializers import BookingSerializer,AdminFlightSerializer
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
class BookingCreateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


    # @action(detail=False, methods=['post'])
    # def create_booking(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
        
    #     departure_location = serializer.validated_data['departure_location']
    #     destination = serializer.validated_data['destination']
    #     adults = serializer.validated_data['adults']
    #     children = serializer.validated_data['children']

    #     try:
    #         flight = Flight.objects.get(departure_location=departure_location, destination=destination)
    #     except Flight.DoesNotExist:
    #         return Response({"detail": "Flight not found"}, status=400)

    #     total_amount = (adults * flight.price) + (children * (flight.price * 0.5))

    #     booking = serializer.save(flight=flight, total_amount=total_amount)
    #     return Response(BookingSerializer(booking).data)



class AdminFlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = AdminFlightSerializer


