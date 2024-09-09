from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from .models import UserModel
from .permissions import IsNotAuthenticated
from django.contrib.auth import login, logout
from rest_framework.response import Response
from rest_framework import status


class RegisterView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsNotAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


@api_view(["POST"])
@permission_classes([IsNotAuthenticated])
def login_view(request):
    data = request.data

    email = data.get('email')
    password = data.get('password')

    try:
        user = UserModel.objects.get(email=email)

        if user.check_password(password):
            login(request, user)
            return Response({
                "message": "You are logged in successfully"
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "Email or password incorrect"
        }, status=status.HTTP_400_BAD_REQUEST)
    except UserModel.DoesNotExist:
        return Response({
            "message":"User doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)

