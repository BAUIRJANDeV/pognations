from django.urls import path

# BU MIXSINGLI CRUDNI IMPORT QILISHI
from .views import ListCreateApi,DetailUpdateDeleteApi

# BU GENERICAPIVEW  IMPORT QILISH
#from .views import ListCreateApiw,DetailUpdateDeleteApi

# FUNKSYA IMPORT QILISHI
#from .views import sumkalar_list,sumkalar_delete,sumka_detail,sumka_create,sumka_update





urlpatterns=[





    # BU MIXSINGLI CRUDNI URLSI
    path('',ListCreateApi.as_view(),name='list'),
    path('i/<int:pk>/',DetailUpdateDeleteApi.as_view(),name='detail'),


    #  BU GENERIC API NING URLSII
    # path('',ListCreateApiw.as_view(),name='list'),
    # path('i/<int:pk>/',DetailUpdateDeleteApi.as_view(),name='pkMos')


    # FUNKSYA URLSSII
    # path('',sumkalar_list,name='list'),
    # path('delete/<int:pk>/',sumkalar_delete,name='delete'),
    # path('detail/<int:pk>/',sumka_detail,name='detail'),
    # path('create/',sumka_create,name='create'),
    # path('update/<int:pk>/',sumka_update,name='update'),
]