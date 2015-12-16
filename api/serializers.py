from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Listing


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ListingSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    price = serializers.IntegerField() #required=False)
    beds = serializers.IntegerField() #required=False)
    baths = serializers.IntegerField() #required=False)
    address = serializers.CharField() #required=False)
    provider_name = serializers.CharField() #required=False)

    def create(self, validated_data):
        # explictly defined for convienience
        return Listing.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # explictly defined for convienience
        instance.price = validated_data.get('price', instance.price)
        instance.beds = validated_data.get('beds', instance.beds)
        instance.baths= validated_data.get('baths', instance.baths)
        instance.address = validated_data.get('address', instance.address)
        instance.provider_name = validated_data.get('provider_name', instance.provider_name)
        instance.save()
        return instance
