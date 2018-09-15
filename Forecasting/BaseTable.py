from __future__ import unicode_literals

from django.http import JsonResponse
from django_pandas.io import read_frame
from rest_framework.views import APIView

from .models import BaseTable


class GetBaseTableAPI(APIView):
    def get(self, request):

        args = {reqobj + '__iexact': request.GET.get(reqobj) for reqobj in request.GET.keys()}

        #To store if session is new or default
        sessionflag_value = args.get('sessionflag__iexact')
        output={}

        print(read_frame(BaseTable.objects.values()))
        skus_df = read_frame(BaseTable.objects.values()).to_json()
        return JsonResponse(skus_df, safe=False)