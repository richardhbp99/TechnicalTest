from django.urls import path
from Subjects import views

urlpatterns = [
    path('list_subjects/', views.SubjectListView.as_view(), name='get-subjects'),
    path('list-pensum/',views.PensumListViews.as_view(),name='get-pensum'),
    path('create-enrollment',views.EnrollmentCreateViews.as_view(),name='create-enrollment'),
    path('students/subjets/<int:student_id>/',views.StudentEnrollmentsList.as_view(), name='student-enrollments-list'),
    path('students/approved-subjects/<int:student_id>/',views.StudentApprovedSubjectsList.as_view(), name='student-approved-subjects-list'),
    
]
