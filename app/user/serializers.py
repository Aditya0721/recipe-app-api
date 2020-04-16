from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _  # when outputting
# a message this will translate to the correct language

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """serializers for the user object"""

    class Meta():
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)
        #  valid_data is the json data passsed into
        #  overriding create function present in ModelSerializer class


class AuthTokenSerializer(serializers.Serializer):
    """create a authentication token object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """validate authenticated user"""
        email = attrs.get('email')  # attrs is every
        # field at the above in the serializer
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,  # parameter required for authenticate
            password=password
        )
        if not user:
            msg = _('unable to authenticate user with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
