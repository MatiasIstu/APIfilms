from django.http import HttpResponse
from django.http import JsonResponse
from ..model.films import costo_pais
from ..model.films import costo_promedio_pais
from rest_framework import permissions
from rest_framework.decorators import api_view
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(methods=['get'],manual_parameters=[openapi.Parameter('pais', openapi.IN_QUERY, description="Coutry to get total budget", type=openapi.TYPE_STRING)])
@api_view(['GET'])
def view_costo_pais(request):
    print("HHOLA")
    print(request.GET['pais'])
    return HttpResponse(costo_pais(request.GET['pais']))

@swagger_auto_schema(methods=['get'],manual_parameters=[openapi.Parameter('pais', openapi.IN_QUERY, description="Coutry to get average budget", type=openapi.TYPE_STRING)])
@api_view(['GET'])
def view_costo_promedio_pais(request):
    return HttpResponse(costo_promedio_pais(request.GET['pais']))

