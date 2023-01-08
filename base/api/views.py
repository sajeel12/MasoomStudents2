from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RoomSerializer
from base.models import Room

from base.api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',                     # decalring api routes
        'GET /api/rooms',                     # decalring api routes
        'GET /api/rooms/:id'
    ]
    return Response(routes)      


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)        #many  for  getting many data not single

    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)        #many  for  getting many data not single

    return Response(serializer.data)