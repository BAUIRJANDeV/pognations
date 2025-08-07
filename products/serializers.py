from  .models import Sumkalar
from rest_framework import serializers
class SumkalarSerializers(serializers.ModelSerializer):
    class Meta:
        model=Sumkalar
        fields='__all__'