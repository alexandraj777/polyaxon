from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import re_path

from api.repos import views
from constants.urls import NAME_PATTERN, USERNAME_PATTERN

urlpatterns = [
    re_path(r'^{}/{}/repo/?$'.format(USERNAME_PATTERN, NAME_PATTERN),
            views.RepoDetailView.as_view()),
    re_path(r'^{}/{}/repo/upload/?$'.format(USERNAME_PATTERN, NAME_PATTERN),
            views.UploadFilesView.as_view()),
    re_path(r'^{}/{}/repo/download/?$'.format(USERNAME_PATTERN, NAME_PATTERN),
            views.DownloadFilesView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
