from django.http import Http404
from rest_framework import mixins, generics, permissions, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.account.api.permissions import OwnProfilePermission
from apps.account.api.serializers import RegisterSerializer, MyUserSerializer, UserProfileSerializer, \
    ChangePasswordSerializer
from apps.base_user.models import MyUser


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": MyUserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class UserProfileView(APIView):
    permission_classes = (IsAuthenticated, OwnProfilePermission,)

    # permission_classes = (AllowAny,)

    # def get_object(self, pk):
    #     try:
    #         return MyUser.objects.get(pk=pk)
    #     except MyUser.DoesNotExist:
    #         raise Http404

    def get(self, request, format=None):
        serializer = UserProfileSerializer(self.request.user, context={'request': self.request})
        return Response(serializer.data)

    def patch(self, request, format=None):  # Partial Update
        serializer = UserProfileSerializer(self.request.user,context={'request': self.request}, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     serializer = UserProfileSerializer(user)
    #     return Response(serializer.data)
    #
    # def patch(self, request, pk, format=None):  # Partial Update
    #     user = self.get_object(pk)
    #     serializer = UserProfileSerializer(user, data=request.data, partial=True)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    """
    An endpoint for changing password.
    """

    permission_classes = (IsAuthenticated, OwnProfilePermission,)

    def get_object(self, pk):
        try:
            return MyUser.objects.get(pk=pk)
        except MyUser.DoesNotExist:
            raise Http404

    def put(self, request, pk, *args, **kwargs):
        user = self.get_object(pk)
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get("new_password"))
            user.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
