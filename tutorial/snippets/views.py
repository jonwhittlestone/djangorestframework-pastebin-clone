from django.http import HttpResponse, JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import mixins, generics
from django.contrib.auth.models import User
from snippets.models import Snippet

from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **args)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class SnippetList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView
                ):
    """
    List all snippets, or create a new snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class=UserSerializer