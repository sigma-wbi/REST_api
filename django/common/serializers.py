from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        # fields = ['url', 'username', 'gender', 'birthday', 'email', 'phone']


class SignupSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'})
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'email', 'gender', 'birthday', 'phone']
    
    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'password are not match!'})
        return attrs
    
    def create(self, validated_data):
        print(validated_data)
        user = get_user_model()(
            username=validated_data['username'],
            # password=validated_data['password1'], 이렇게 하면 raw_data로 들어감
            email=validated_data.get('email', ''),
            gender=validated_data.get('gender', ''),
            birthday=validated_data.get('birthday'),
            phone=validated_data.get('phone', ''),
        )
        user.set_password(validated_data['password1']) # 이렇게 해야 암호화됨
        user.save()
        return user
    