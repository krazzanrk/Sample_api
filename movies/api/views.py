from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser,MultiPartParser
from rest_framework.response import Response

from .serializers import GenreSerializer, FilmSerializer
from ..models import Genre, Film
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView


class GenreCreateAPIView(ListAPIView, CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GenreUpdateAPIView(RetrieveAPIView, UpdateAPIView):
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Genre.objects.all()
    lookup_field = 'id'


class FilmCreateAPIView(ListAPIView, CreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = FilmSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by_id=self.request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



