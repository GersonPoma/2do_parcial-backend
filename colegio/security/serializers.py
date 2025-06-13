from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, AuthUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: AuthUser):
        token = super().get_token(user)

        token['user_id'] = user.id
        token['rol'] = user.rol

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data['user_id'] = self.user.id
        data['rol'] = self.user.rol

        return data