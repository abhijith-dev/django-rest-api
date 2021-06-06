from rest_framework.views import APIView
from rest_framework.response import Response
class Demo(APIView):
    def get(self,request,day,location):
        return Response({"response_day":day,"response_location":location})
        