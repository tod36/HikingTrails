from django.urls import path

from .views import book_recommendation_view, like_recommendation_view, recommendation_list_view, \
    delete_recommendation_view

urlpatterns = [
    path('book-recommendation/', book_recommendation_view, name='book_recommendation'),
    # path('recommendation-success/', TemplateView.as_view(template_name='recommendation_success.html'), name='recommendation_success'),

    path('recommendation/delete/<int:pk>/', delete_recommendation_view, name='delete_recommendation'),

    path('recommendations/', recommendation_list_view, name='recommendation_list'),
    path('like-recommendation/<int:pk>/', like_recommendation_view, name='like_recommendation'),
]
