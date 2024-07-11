from django.urls import path
from . import views

urlpatterns = [
    # path('<int:number_post>', views.posts_inf_number),
    # path('<slug:slug_blog>', views.posts_inf, name='one_blog_info'),
    path('', views.HomePageView.as_view(), name='home_page'),
]
