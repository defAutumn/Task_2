from rest_framework import views,response,permissions
from serializer import CustomUserSerializer

class RegisterApi(views.APIView):

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        print(data)

        return response.Response(data={'hello': 'world'})