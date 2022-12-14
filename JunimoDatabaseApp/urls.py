from django.urls import path

from JunimoDatabaseApp.views.blueprint_views import BlueprintView, BlueprintDetail
from .views.character_views import Characters, CharacterDetail
from .views.material_views import Materials, MaterialDetail
from .views.recipe_material_views import RecipeMaterialDetailView, RecipeMaterialsView
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.inventory_views import ShowInventoryView, InventoryDetail

urlpatterns = [
    # Restful routing
    path('characters/', Characters.as_view(), name='characters'),
    path('characters/<int:pk>/', CharacterDetail.as_view(), name='character_detail'),
    path('blueprints/', BlueprintView.as_view(), name='blueprints'),
    path('blueprints/<int:pk>/', BlueprintDetail.as_view(), name='blueprint_detail'),
    path('materials/', Materials.as_view(), name='materials'),
    path('materials/<int:pk>/', MaterialDetail.as_view(), name='material_detail'),
    path('recipe_materials/<int:pk>/', RecipeMaterialsView.as_view(), name='recipe_materials'),
    path('recipe_materials/show/<int:pk>', RecipeMaterialDetailView.as_view(), name='single_recipe_material'),
    # index - all inventory
    path('inventory/<int:pk>/', InventoryDetail.as_view(), name='inventory'),
    # get - one inventory
    path('inventory/<int:pk>/<int:fk>', ShowInventoryView.as_view(), name='show_single_inventory'),
    # for patch/delete
    path('inventory/edit/<int:pk>/<int:fk>', ShowInventoryView.as_view(), name='patch_single_inventory'),
    # for post/delete
    path('inventory/create/<int:pk>', ShowInventoryView.as_view(), name='create_inventory'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
