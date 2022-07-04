from django.shortcuts import render
from django.utils.decorators import method_decorator

from .models import Test
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import tableserializer
from django.views.decorators.csrf import csrf_exempt
from .consumers import TableConsumer
from .db_connection import updatetable


# Create your views here.


@csrf_exempt
def index(request):

    global update
    if request.method == 'POST':
        updatetable()
        s = TableConsumer()
        s.stream('tableupdate')

        # s = TableConsumer()
        # s.sendsmth()

    table = Test.objects.all()
    context = {
        'table': table
    }
    return render(request, 'table/index.html', context)

@api_view(['GET'])
def getroutes(request):
    routes = [
        {
            'Endpoint': '/Tables/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/Table/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/Table/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/Table/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/Table/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
# @method_decorator(csrf_exempt, name=dispatch)
def gettable(request):
    tables = Test.objects.all()
    serializer = tableserializer(tables, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @method_decorator(csrf_exempt, name=dispatch)
def gettableone(request, pk):
    tables = Test.objects.filter(id=pk)
    serializer = tableserializer(tables, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
# @method_decorator(csrf_exempt, name=dispatch)
def updateTable(request, pk):
    data = request.data
    tables = Test.objects.filter(id=pk)
    serializer = tableserializer(instance=tables, many=False)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)