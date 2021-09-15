
from django.urls import path
from .import views

urlpatterns = [
    path('h/',views.homeView,name='home'),
    path('add_dept/', views.addView,name='add_dept'),
    path('showdpt/', views.showdeptView, name='showdpt'),
    path('up/<int:id1>/', views.updateView, name='up'),
    path('de/<int:id1>/', views.deleteView, name='de'),

    path('add_stu/', views.add_Stu_View,name='add_stu'),
    path('show_stu/',views.show_Stu_View,name='show_stu'),
    path('up_stu/<int:id1>/', views.update_Stu_View, name='up_stu'),
    path('de_stu/<int:id1>/', views.delete_Stu_View, name='de_stu'),

    path('add_lec/', views.add_Lec_View,name='add_lec'),
    path('show_lec/',views.show_lec_View,name='show_lec'),
    path('up_lec/<int:id1>/', views.update_Lec_View, name='up_lec'),
    path('de_lec/<int:id1>/', views.delete_Lec_View, name='de_lec'),

    path('search/', views.search, name='search'),
    # path('se_stu/<int:id1>/', views.search_dept_stu, name='se_stu'),
    # path('se_lec/<>int:id1>/', views.search_dept_lect, name='de_lec')

]
