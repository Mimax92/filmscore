from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from filmscore.views import CreateUser
from rest_framework import routers
from filmscore.views import UserView, FilmView

router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'films', FilmView)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('films/', include('filmscore.urls')),
                  path('login/', auth_views.LoginView.as_view(), name="login"),
                  path('logout/', auth_views.LogoutView.as_view(), name="logout"),
                  path('createuser/', CreateUser.as_view(), name="create-user"),
                  path('', include(router.urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
