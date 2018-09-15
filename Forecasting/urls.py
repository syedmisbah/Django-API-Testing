from django.conf.urls import url
from rest_framework import routers

from . import api
from .BaseTable import GetBaseTableAPI

router = routers.DefaultRouter()
router.register(r'basetable', api.BaseTableViewSet)

urlpatterns = [
    url(r'^CalltoAPI', GetBaseTableAPI.as_view(), name='CalltoAPI')
]



# urlpatterns = (
#     # urls for Django Rest Framework API
#     path('api/v1/', include(router.urls)),
#     url(r'^Forecasting/basetablecallapi', GetBaseTableAPI.as_view(), name='Forecasting Base Table API')
# )
#
# urlpatterns += (
#     # urls for BaseTable
#
#     path('Forecasting/basetable/', views.BaseTableListView.as_view(), name='Forecasting_basetable_list'),
#     path('Forecasting/basetable/create/', views.BaseTableCreateView.as_view(), name='Forecasting_basetable_create'),
#     path('Forecasting/basetable/detail/<slug:slug>/', views.BaseTableDetailView.as_view(), name='Forecasting_basetable_detail'),
#     path('Forecasting/basetable/update/<slug:slug>/', views.BaseTableUpdateView.as_view(), name='Forecasting_basetable_update'),
# )

