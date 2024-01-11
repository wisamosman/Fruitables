from .serializers import FruitSerializer
from .models import Fruit
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics



@api_view(['GET'])
def fruit_list_api(request):
    fruit = Fruit.objects.all()[:10]
    data = FruitSerializer(fruit,many=True,context=({'request':request})).data
    

    return Response({'data':data})


class FruitDetailAPI(generics.RetrieveDestroyAPIView):
     queryset = Fruit.objects.all()
     serializer_class = FruitSerializer
