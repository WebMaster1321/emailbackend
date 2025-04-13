from rest_framework  import serializers


class EmailSerializer(serializers.Serializer):
    sender_name = serializers.CharField(max_length=255)  # Name des Absenders
    sender_email = serializers.EmailField()  # E-Mail des Absenders
    subject = serializers.CharField(max_length=255)  # Betreff
    message = serializers.CharField()  # Nachricht     

