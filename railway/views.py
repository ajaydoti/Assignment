# railway/views.py

from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import Train
from .serializers import TrainSerializer
# railway/views.py

from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class =TrainSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
