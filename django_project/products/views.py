from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductSerializer 




class ProductView(APIView):
    def get(self, request):
        serializer = ProductSerializer(data=request.GET)
        if serializer.is_valid():
            product_search_queryset = serializer.search()
            serialize = ProductSerializer(product_search_queryset, many=True)
            return Response(serialize.data)
        else:
            return Response(serializer.errors)




