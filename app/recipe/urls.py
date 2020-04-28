from django.urls import path, include
from rest_framework.routers import DefaultRouter
# automatic registers all the urls for all the actions in the view set
from recipe import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
