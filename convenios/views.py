from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Convenio
from .serializers import RetrieveUpdateDestroySerializer
from .mixins import SerializeByMethodMixin
from convenios.permissions import isSuperUser

class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    permission_classes = [isSuperUser]

    queryset = Convenio.objects.all()
    serializer_class = RetrieveUpdateDestroySerializer

class CreateConvenioView( ListCreateAPIView):

    permission_classes = [isSuperUser]

    queryset = Convenio.objects.all()
    
    serializer_class = RetrieveUpdateDestroySerializer

