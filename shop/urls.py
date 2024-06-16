from django.urls import path

from shop.views import (
    CategoriesListView,
    CategoryDetailView,
    ProductDetailView,
    ProductsListView,
)

urlpatterns = [
    path("categories", CategoriesListView.as_view(), name="categories-list"),
    path("category/<int:pk>", CategoryDetailView.as_view(), name="category-detail"),
    path("products", ProductsListView.as_view(), name="products-list"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product-detail"),
]
