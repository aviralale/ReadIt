from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # API TO COMMENT
    path('postcomment', views.postComment, name ="postComment"),
    path('',views.blogHome,name='blogHome'),
    path('<str:slug>',views.blogPost,name='blogPost'),
    path('category/world/', views.category_world, name='category_world'),
    path('category/miscellaneous/', views.category_miscellaneous, name='category_miscellaneous'),
    path('category/technology/', views.category_technology, name='category_technology'),
    path('category/design/', views.category_design, name='category_design'),
    path('category/culture/', views.category_culture, name='category_culture'),
    path('category/business/', views.category_business, name='category_business'),
    path('category/politics/', views.category_politics, name='category_politics'),
    path('category/opinion/', views.category_opinion, name='category_opinion'),
    path('category/science/', views.category_science, name='category_science'),
    path('category/programming/', views.category_programming, name='category_programming'),
    path('category/style/', views.category_style, name='category_style'),
    path('category/travel/', views.category_travel, name='category_travel'),
    path('archive/<int:year>/<int:month>', views.archive_posts, name='archive_posts'),
]
