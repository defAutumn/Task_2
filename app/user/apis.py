from rest_framework import views,response, exceptions, permissions
from . import serializer as user_serializer
from . import services, authentication


class RegisterApi(views.APIView):

    def post(self, request):
        serializer = user_serializer.CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_user(user_dc=data)

        return response.Response(data=serializer.data)


class LoginApi(views.APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = services.user_mail_selector(email=email)

        if user is None:
            raise exceptions.AuthenticationFailed('Invalid Credentials')

        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed('Invalid Credentials')

        token = services.create_token(user_id=user.id)

        resp = response.Response()

        resp.set_cookie(key='jwt', value=token, httponly=True)

        return resp


class UserApi(views.APIView):
    """
    This endpoint can only be used
    if the user is authenticated
    """
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user

        serializer = user_serializer.CustomUserSerializer(user)

        return response.Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = user_serializer.UserPutSerializer(user, data=request.data)  # use new serializer here
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors)

    def delete(self, request):
        user = request.user
        user.delete()

        return response.Response({"result": "user delete"})

class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie('jwt')
        resp.data = {'message': 'bye'}

        return resp