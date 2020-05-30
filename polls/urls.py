from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('kanmusu_syousai/<int:kanmusu_id>/vote/', views.vote, name='vote'),
    path('kanmusu', views.index2, name='index2'),
    path('kanmusu2', views.kanmusu_list, name='kanmusu_list'),
    path('kanmusu3', views.kanmusu_list2, name='kanmusu_list2'),
    path('kanmusu/<int:oogata_id>/', views.kanmusu_by_type, name='kanmusu_by_type'),
    path('kanmusu_syousai/<int:kanmusu_id>/', views.detail2, name='detail2'),
    path('seiyu', views.detail3, name='detail3'),
    path('seiyu/<int:seiyu_id>/', views.seiyu_syousai, name='seiyu_syousai'),
    path('seiyu/<int:seiyu_id>/tanto', views.seiyu_tanto ,name='seiyu_tanto'),
    path('kansyu',views.kansyu, name='kansyu'),
    path('kansyu/<int:kansyu_id>',views.kansyu_by_type, name='kansyu_by_type'),
    path('map_list',views.battle_name, name='map_list'),
    path('sanka_kanmusu/<int:battle_id>',views.sanka_kanmusu, name = 'sanka_kanmusu'),
    path('ivent', views.ivent, name='ivent'),
    path('ivent_naiyou/<int:name_id>',views.ivent_naiyou, name = 'ivent_naiyou'),####name_idはIventモデルの名前のこと
    path('nikkicreate',views.NikkiCreateView.as_view(),name='nikkicreate'),#フォーム
    path('nikkilist',views.NikkiListView.as_view(),name='nikkilist'),#リスト
    path('nikki/search',views.NikkiListQueryView.as_view(),name='nikkisearch'),#検索
    path('nikki/tagsearch/<int:pk>',views.NikkiTagListQueryView.as_view(),name='nikkitagsearch'),#タグ検索
    path('nikki/<int:pk>',views.NikkiDitaltView.as_view(),name='nikki'),#日記詳細
    path('commentcreate/<int:pk>/',views.CommentCreateView.as_view(),name='commentcreate'),#コメントフォーム
    path('questioncreate',views.QuestionCreateView.as_view(),name='questioncreate'),#質問フォーム
    path('question/<int:pk>',views.QuestionDitaltView.as_view(),name='question'),#質問詳細
    path('answercreate/<int:pk>/',views.AnswerCreateView.as_view(),name='answercreate'),#質問解答フォーム
    path('playquestion_list',views.QuestionListView.as_view(),name='question_list'),#質問リスト
    path('<int:answer_id>/like/', views.like, name='like'),
    path('<int:kanmusu_id>/kanmusu_ninnki/', views.kanmusu_ninnki, name='kanmusu_ninnki'),
    path('graph', views.graph, name='graph'),
    path('graph2', views.graph2, name='graph2'),
    path('api_map/<int:map_id>', views.api_map, name='api_map'),
   ]
                