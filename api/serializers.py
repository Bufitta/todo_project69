import re
from rest_framework import serializers
from tasks.models import Category, Task, Attachment, User


class CategorySerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'tasks']


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='api:task-detail')
    priority = serializers.ReadOnlyField(source='get_priority_display')
    category = serializers.HyperlinkedRelatedField(view_name='api:category-detail', queryset=Category.objects.all())
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    category_name = serializers.ReadOnlyField(source='category.title')

    class Meta:
        model = Task
        fields = ['id', 'title', 'deadline', 'description', 'done', 'priority', 'category', 'user', 'category_name']


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

    def validate_email(self, value):
        print('validate_email')
        if not re.match(r'^[\w.\-]{1,25}@yandex\.(by|ru|ua|com)$', value):
            raise serializers.ValidationError('wrong email')
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('user exists')
        return value

    def validate(self, data):
        print('validate')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        if not any([first_name, last_name]):
            raise serializers.ValidationError('first or last name is required')
        return data


class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment
        fields = ['id', 'file']
