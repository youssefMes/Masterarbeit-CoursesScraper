from rest_framework import serializers
from .models import Bookmark, Information, Percentage, Portal, Star, User, Course, Comment, Logo
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['image']

class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = '__all__'

class PercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Percentage
        fields = '__all__'

class PortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portal
        fields = ('name', 'link')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_active', 'is_staff')

class CourseSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(source='comment_set', many=True)
    stars = StarSerializer(source='star_set', many=True)
    percentages = PercentageSerializer(source='percentage_set', many=True)
    information = InformationSerializer(required=True)
    portal = PortalSerializer(required=True)
    logo = LogoSerializer()
    validated_by = UserSerializer()
    invalidated_by = UserSerializer()
    class Meta:
        model = Course
        fields = ('id' ,'name' , 'evaluation_count', 'information', 'link', 'portal', 'comments', 'stars', 'percentages', 'logo', 'is_valid', 'validated_by', 'invalidated_by')

class BookmarkSerializer(serializers.ModelSerializer):
    course_name = serializers.ReadOnlyField(source='course.name')
    university = serializers.ReadOnlyField(source='course.information.university')
    logo = serializers.ReadOnlyField(source='course.logo.image')
    class Meta:
        model = Bookmark
        fields = ('user' ,'course_name','university', 'course', 'logo', 'id')
        extra_kwargs = {
            'user': {'write_only': True},
        }

class UserCreateSerializer(BaseUserCreateSerializer):
    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)
    
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('password','first_name', 'last_name', 'email', 'is_active', 'is_staff')