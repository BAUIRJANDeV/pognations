from rest_framework.views import APIView
from django.db.models import Q
from django.template.context_processors import request
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from unicodedata import category
from rest_framework.generics import GenericAPIView,mixins
from  .models import Sumkalar,Category
from .serializers import SumkalarSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination


class ListCreateApi(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    GenericAPIView):
    queryset = Sumkalar.objects.all()
    serializer_class = SumkalarSerializers
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['categorys']
    search_fields = ['rangi', 'hajmi']
    ordering_fields = ['narhi']
    ordering = ['narhi']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DetailUpdateDeleteApi(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            GenericAPIView):
    queryset = Sumkalar.objects.all()
    serializer_class = SumkalarSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)













# class ListCreateApiw(GenericAPIView):
#     queryset = Sumkalar.objects.all()
#     serializer_class = SumkalarSerializers
#
#     def get(self,request):
#         sumkalar=Sumkalar.objects.all()
#         category=request.GET.get('category')
#         if category:
#             sumkalar=sumkalar.filter(name__icontains=category)
#         search=request.GET.get('search')
#         if search:
#             sumkalar=sumkalar.filter(Q(rangi__icontains=search) | Q(hajmi__icontains=search))
#         serializer=SumkalarSerializers(sumkalar,many=True)
#         res={
#             'data':serializer.data,
#             'count':len(sumkalar),
#             'status':status.HTTP_200_OK
#         }
#         return Response(res)
#
#     def post(self,request):
#         serializer=SumkalarSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#
#
# class DetailUpdateDeleteApi(GenericAPIView):
#     queryset = Sumkalar.objects.all()
#     serializer_class = SumkalarSerializers
#
#     def get_object(self, pk):
#         sumka = Sumkalar.objects.get(id=pk)
#         return sumka
#
#
#     def get(self,request,pk):
#         sumka=Sumkalar.get_object(id=pk)
#         serializer=SumkalarSerializers(sumka)
#         res={
#             'data':serializer.data,
#             'status':status.HTTP_200_OK
#         }
#         return Response(res)
#
#
#     def put(self,request,pk):
#         sumka=Sumkalar.objects.get(id=pk)
#         serializer=SumkalarSerializers(sumka,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status.HTTP_200_OK)
#         return Response(serializer.errors)
#
#     def delete(self,request,pk):
#         sumka=Sumkalar.objects.get(id=pk)
#         sumka.delete()
#         return Response(status=status.HTTP_200_OK)
#
#     def patch(self,request,pk):
#         sumka = Sumkalar.objects.get(id=pk)
#         serializer = SumkalarSerializers(sumka, data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status.HTTP_200_OK)
#         return Response(serializer.errors)
















# @api_view(['GET'])
# def sumkalar_list(request):
#     sumkalar=Sumkalar.objects.all()
#     category=request.GET.get('category')
#     if category:
#         sumkalar=Sumkalar.objects.filter(name__icontains=category)
#     search=request.GET.get('search')
#     if search:
#         sumkalar=Sumkalar.objects.filter(Q(rangi__icontains=search) | Q(narhi=search))
#
#     serializer=SumkalarSerializers(sumkalar,many=True)
#     res={
#         'data':serializer.data,
#         'count':len(sumkalar),
#         'status':status.HTTP_200_OK
#     }
#     return Response(res)
#
# @api_view(['GET'])
# def sumka_detail(request,pk):
#     sumka=Sumkalar.objects.get(id=pk)
#     serializer=SumkalarSerializers(sumka)
#     res={
#         'data':serializer.data,
#         'status':status.HTTP_200_OK,
#     }
#     return Response(res)
#
# @api_view(['DELETE'])
# def sumkalar_delete(request,pk):
#     suumka=Sumkalar.objects.get(id=pk)
#     suumka.delete()
#     return Response(status.HTTP_200_OK)
#
# @api_view(['POST'])
# def sumka_create(request):
#     serializer=SumkalarSerializers(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)
#
# @api_view(['PUT','PATCH'])
# def sumka_update(request,pk):
#     sumka=Sumkalar.objects.get(id=pk)
#     serializer=SumkalarSerializers(sumka,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)