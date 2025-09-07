
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer
from .tasks import send_welcome_email

class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all().order_by('-created_at')
    serializer_class = ListingSerializer
    
class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    
    
    
@api_view(["POST"])
def trigger_email(request):
    user_email = request.data.get("email")
    if not user_email:
        return Response({"error": "Email is required"}, status=400)

    # Call Celery task asynchronously
    task = send_welcome_email.delay(user_email)

    return Response({
        "message": f"Task started for {user_email}",
        "task_id": task.id
    })

    
# @api_view(["POST"])
# def trigger_email(request):
#     user_email = request.data.get("email")
#     if user_email:
#         return Response({"message": "Email task triggered."}, status=status.HTTP_200_OK)
#     return Response({"error": "Email not provided."}, status=status.HTTP_400_BAD_REQUEST)

#    return Response({
#        "message": f"Task started for {user_email}"
#        "task_id": task.id
#    })
# class HelloWorldView(APIView):
#     def get(self, request):
#         return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)
    