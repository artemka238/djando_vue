from rest_framework import serializers
from django.contrib.auth.models import User
# from rest_framework_simplejwt.tokens import RefreshToken

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id","username","password","token")
#         # fields = ("id","username","password")

#     token = serializers.SerializerMethodField()
#     password = serializers.CharField(write_only = True)

#     def get_token(self,user):
#         refresh = RefreshToken.for_user(user)
#         return {
#             "refresh":str(refresh),
#             "access":str(refresh.access_token)
#         }
    
#     def create(self,validated_data):
#         # password = validated_data.pop("password",None)
#         # instance = self.Meta.model(**validated_data)
#         # if(password is not None):
#         #     instance.set_password(password)
#         #     instance.save()
#         #     return instance
#         user = User.objects.create(
#             username = validated_data["username"],
#             password = validated_data["password"]
#         )
#         return user

        
    # def update(self,instance,validated_data):
    #     password = validated_data.pop("pasword",None)
    #     user = super().update(instance,validated_data)
    #     if(password):
    #         user.set_password(password)
    #         user.save()
    #     return user