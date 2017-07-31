from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from . import serializers


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupsSerializer
