from rest_framework.views import APIView, status, Response, Request
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsCurrentUserAndEmployee
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        IsAuthenticated,
        IsCurrentUserAndEmployee,
    ]

    def get(self, req: Request, user_id: int) -> Response:
        founded_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(req, founded_user)
        serializer = UserSerializer(founded_user)

        return Response(serializer.data)

    def patch(self, req: Request, user_id: int) -> Response:
        founded_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(req, founded_user)

        serializer = UserSerializer(
            founded_user,
            data=req.data,
            partial=True,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
