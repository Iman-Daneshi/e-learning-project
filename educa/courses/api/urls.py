from django.urls import path, include
from rest_framework import routers
from .views import SubjectDetailView, SubjectListView, CourseEnrollView, CourseViewSet

app_name = 'courses'

router = routers.DefaultRouter()
router.register('courses', CourseViewSet)

urlpatterns = [
  path('subjects/', SubjectListView.as_view(), name='subject_list'),
  path('subjects/<pk>/', SubjectDetailView.as_view(), name='subject_detail'),
  # path('courses/<pk>/enroll/', CourseEnrollView.as_view(), name='course_enroll'),
  path('', include(router.urls)),
  ]