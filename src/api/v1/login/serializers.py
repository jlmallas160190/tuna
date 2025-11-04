from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise serializers.ValidationError("Credenciales inválidas.")
            if not user.is_active:
                raise serializers.ValidationError("Este usuario está inactivo.")
        else:
            raise serializers.ValidationError("Debe proporcionar correo y contraseña.")

        data["user"] = user
        return data
