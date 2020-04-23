from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from classroom.models import Quiz, Question

# Serializers define the API representation.

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['text', ]


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['name', 'subject', 'questions']


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'quizes', QuizViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.