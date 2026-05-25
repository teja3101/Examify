from django.urls import path
from . import views

urlpatterns = [

    # ================= HOME =================
    path('', views.Home, name='home'),

    # ================= QUESTION MODULE =================
    path('questioncurd/', views.QuestionCurdPage, name='question_curd'),

    path('create-question/', views.CreateQuestion, name='create_question'),

    path('show-questions/', views.ShowAllQuestion, name='show_questions'),

    path('show-update-question/', views.ShowQuestionforUpdate, name='show_update_question'),

    path('update-question/<int:qno>/', views.UpdateQuestion, name='update_question'),

    path('show-delete-question/', views.ShowQuestionforDelete, name='show_delete_question'),

    path('delete-question/<int:qno>/', views.DeleteQuestion, name='delete_question'),

    # ================= USER MODULE =================
    path('userdashboard/', views.ShowUserforCurdPage, name='user_dashboard'),

    path('create-user/', views.CreateUser, name='create_user'),

    path('update-user/<int:uid>/', views.UpdateUser, name='update_user'),

    path('delete-user/<int:uid>/', views.DeleteUser, name='delete_user'),

    # ================= LOGIN / LOGOUT =================
    path('loginuser/', views.LoginUser, name='login_user'),

    path('logoutuser/', views.LogoutUser, name='logout_user'),

    # ================= TEST MODULE =================
    path('subject/', views.subject, name='subject'),

    path('start-test/', views.StartTest, name='start_test'),

    path('next-question/', views.NextQuestion, name='next_question'),

    path('end-test/', views.EndTest, name='end_test'),
]