from rest_framework.views import APIView, status, Response, Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrReadOnly
from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def post(self, req: Request) -> Response:
        serializer = MovieSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=req.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        all_movies = Movie.objects.all()
        result = self.paginate_queryset(all_movies, req)
        serializer = MovieSerializer(result, many=True)

        return self.get_paginated_response(serializer.data)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, req: Request, movie_id: int) -> Response:
        founded_movie = get_object_or_404(Movie, pk=movie_id)
        self.check_object_permissions(req, founded_movie)
        serializer = MovieSerializer(founded_movie)

        return Response(serializer.data)

    def delete(self, req: Request, movie_id: int) -> Response:
        founded_movie = get_object_or_404(Movie, pk=movie_id)
        self.check_object_permissions(req, founded_movie)
        founded_movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
