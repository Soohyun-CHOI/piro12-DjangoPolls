from django.urls import path

from polls import views

app_name = "polls"

urlpatterns = [
    path("", views.IndexView, name="index"),
    path("<int:pk>/", views.DetailView, name="detail"),
    path("<int:pk>/result/", views.ResultsView, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]