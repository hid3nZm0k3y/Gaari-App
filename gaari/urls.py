from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'gaari'

urlpatterns = [
    path("", views.index, name="home"),
    path("favorites", login_required(views.view_favorite), name="view_favorite"),
    path("inbox", login_required(views.view_inbox), name="view_inbox"),
    path("inbox/<int:pk>", login_required(views.message_delete), name="message_delete"),

    path("autos", views.AutosCreateView.as_view(), name="autos"),
    path("autos/<int:pk>", views.AutosListView.as_view(), name="autos_list"),
    path("autos/<int:pk>/update/", views.AutosUpdateView.as_view(), name="autos_update"),
    path("autos/<int:pk>/delete/", views.AutosDeleteView.as_view(), name="autos_delete"),

    path("autos/<int:pk>/review", views.ReviewCreateView.as_view(), name="review"),
    path("autos/<int:pk>/review/<int:review_pk>", views.ReviewDelete, name="review_delete"),

    path("autos/<int:pk>/favorite", views.favorite, name="favorite"),

    path("make", views.MakeCreateView.as_view(), name="make"),
    path('make/<int:pk>/update/', views.MakeUpdateView.as_view(), name='make_update'),
    path('make/<int:pk>/delete/', views.MakeDeleteView.as_view(), name='make_delete'),
    path("thank-you", views.thank_you)
]
