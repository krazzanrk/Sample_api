from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies.api.serializers import RegistrationSerializer


@api_view(["POST"])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()

            data["response"] = "sucessufully registered new user"
            data["email"] = account.email
            data["username"] = account.username
            token=Token.objects.get(user=account).key
            data["token"]=token
        else:
            data = serializer.errors
        return Response(data)