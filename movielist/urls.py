from django.urls import include, path
from movies.views import MovieView

urlpatterns = [
    path("unicorn/", include("django_unicorn.urls")),
    path('', MovieView.as_view()),
]
