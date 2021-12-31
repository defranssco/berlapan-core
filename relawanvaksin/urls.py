from django.urls import path
from django.urls.conf import include

from .views import detail_relawan_vaksin, lihat_data_relawan_vaksin,index,MainView,PostJsonListView,serialisasi,add_to_django,relawanVaksin

from rest_framework import routers
# from Module_relawan_vaksin.views import MainView, PostJson

app_name = 'Module_relawan_vaksin'

router = routers.DefaultRouter(trailing_slash=False)
router.register('dataRelawanVaksinJson', serialisasi)

router.register(r'datarelawanvaksinjson', relawanVaksin )

#Url untuk page daftar dan melihat data relawan vaksin
urlpatterns = [
    path('', index, name='index'),
    path('lihat_data_relawan_vaksin/',lihat_data_relawan_vaksin.as_view(), name="data-relawan-vaksin"),
    path('detail_relawan_vaksin/<int:pk>', detail_relawan_vaksin.as_view(),name="detail-relawan-vaksin"),
    path('data_relawan_vaksin_singkat/', MainView.as_view(),name='main-view'),
    path('data_relawan_vaksin_singkat/data_relawan_json/<int:num_posts>/', PostJsonListView.as_view(),name='data-relawan-json-view'),

    path('', include(router.urls)),
    path('add_to_django/', add_to_django, name='add_to_django'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]