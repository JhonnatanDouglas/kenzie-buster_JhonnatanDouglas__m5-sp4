from rest_framework.views import APIView, status, Response, Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from movies.models import Movie
from .serializers import MovieOrderSerializer


class MovieOrdersView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, req: Request, movie_id: int) -> Response:
        founded_movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieOrderSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=founded_movie, user=req.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
