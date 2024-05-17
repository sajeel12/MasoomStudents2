from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import RoomSerializer
from base.models import Room
from base.api import serializers

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'POST /api/key'  # Adding new route
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)  # many for getting many data, not single
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)  # many for getting many data, not single
    return Response(serializer.data)

@api_view(['POST'])
def getKey(request):
    data = JSONParser().parse(request)
    key = data.get('key')
    if key is not None:
        if key == '7e40a8997a82494813142b2b9491261ccf2d806a78f2009edeef663681e531bf':   # change this key to stop jazz cash
            return Response({'key': key})
        else:
            return Response({'key': 'nonononononnonsss###$$$%^&*&^%$#ssssssssssssssooooooooooooo2222222222222222233333333333'}, )


    else:
        return Response({'error': 'some error'}, status=400)

@api_view(['POST'])
def oneAppJazzCashKey(request):
    data = JSONParser().parse(request)
    key = data.get('key')
    if key is not None:
        if key == '372db280419bc0ad24e09ecd3ea249ef5be8fb9d3435f3ea53f552160f9c4777':   # change this key to stop jazz cash One app version
            return Response({'key': key})
        else:
            return Response({'key': 'nonononononnonsss###$$$%^&*&^%$#ssssssssssssssooooooooooooo2222222222222222233333333333'}, )


    else:
        return Response({'error': 'some error'}, status=400)

