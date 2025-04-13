from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .serializer import EmailSerializer
# Create your views here.


@api_view(["POST","GET"])
def contact_view(request):

    if request.method == "GET":
       return Response({"message": "Kontakt-API läuft! Verwenden Sie POST, um eine E-Mail zu senden."}, status=status.HTTP_200_OK)


    if request.method == "POST":
        serializer = EmailSerializer(data=request.data)

        if serializer.is_valid():
         sender_name = serializer.validated_data["sender_name"]
         sender_email = serializer.validated_data["sender_email"]
         subject = serializer.validated_data["subject"]
         message = serializer.validated_data["message"]

         full_message = f"Name: {sender_name}\nE-Mail: {sender_email}\n\nNachricht:\n{message}"

         recipient = settings.EMAIL_HOST_USER  # Deine eigene E-Mail-Adresse aus settings.py

        try:
            send_mail(
                subject,
                full_message,
                sender_email,  # Absender (muss oft mit SMTP-Server übereinstimmen)
                [recipient]
            )
            return Response({"message": "E-Mail erfolgreich gesendet!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





