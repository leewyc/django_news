from django.conf.urls import url,include
from . import views
from rest_framework import routers
from yc_list import views


router = routers.DefaultRouter()
#router.register(r'users',views.UserViewSet)
#router.register(r'groups',views.GroupSerializer)

router.register(r'user',views.UserViewSet, base_name='user')
router.register(r'group', views.GroupViewSet, base_name='group')
router.register(r'List', views.ListViewSet, base_name='List')
#router.register(r'hello',views.HelloWorldViewSet,base_name="hello")

urlpatterns = [
    url(r'^list/',views.yc_list),
    url(r'^create_list/',views.yc_sumbit), # 下面的不用
    url(r'^yc_create/',views.yc_create),
    url(r'^',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    #url(r'^get/$',views.post_list,name='api_posts'),
    #url(r'hello/',views.HelloWorldViewSet('hello')),
 ]
#urlpatterns=routers.url
#print("______1")
#urlpatterns=router.urls
#print(urlpatterns)

