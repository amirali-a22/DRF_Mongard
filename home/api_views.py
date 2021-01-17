from rest_framework import viewsets

from home.models import Person
from home.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    # def list(self, request):
    #     # persons = Person.objects.all()
    #     queryset = Person.objects.all()
    #     ser_data = PersonSerializer(queryset, many=True)
    #     return Response(ser_data.data)
    #
    # def retrieve(self, request, pk=None):
    #     # queryset = Person.objects.all()
    #     # person = get_object_or_404(queryset, pk=pk)
    #     # ser_data = PersonSerializer(person)
    #     # if ser_data.is_valid():
    #     #     return Response(ser_data.data)
    #     # return Response(ser_data.errors)
    #     #################
    #     # queryset = Person.objects.all()
    #     # person = get_object_or_404(queryset, pk=pk)
    #     # ser_data = PersonSerializer(person)
    #     # return Response(ser_data.data)
    #     ##########################
    #     try:
    #         queryset = Person.objects.all()
    #         person = get_object_or_404(queryset, pk=pk)
    #     except Person.DoesNotExist:
    #         return Response({'error': 'this user does not exist'})
    #     ser_data = PersonSerializer(person)
    #     return Response(ser_data.data)
    #
    # def create(self, request):
    #     ser_data = PersonSerializer(data=request.data)
    #     if ser_data.is_valid():
    #         ser_data.save()
    #         return Response({'message': 'ok'})
    #     return Response(ser_data.errors)
