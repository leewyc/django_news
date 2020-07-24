#coding:utf-8
from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import *
from django.shortcuts import render,redirect
from hashlib import sha1
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from yc_list.serializers import  UserSerializer,GroupSerializer
from .serializers import   *
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import  APIView



'''
class HelloWorldViewSet(viewsets.GenericViewSet):

    def world(self,request,*args,**kwargs):
        return Response({"code":0,"msg":"hello world!"})
        '''
'''
#@csrf_exempt
def post_list(request):
    if request.method=='GET':
        post = views.objects.filter()
        serializers = UserViewSet(post,many=True)
        return JsonResponse(serializers.data,safe=False)
'''
class UserViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        #serializer_class = UserSerializer
        return User.objects.all()


class GroupViewSet(viewsets.ModelViewSet):
    #queryset = Group.objects.all()
    serializer_class = GroupSerializer
    def get_queryset(self):
        #serializer_class = GroupSerializer
        return Group.objects.all()
     #   ueryset = Group.objects.all()
     #   serializer_class = GroupSerializer



class ListViewSet(viewsets.ModelViewSet):
    #queryset = Group.objects.all()
    serializer_class = ListSerializer
    def get_queryset(self):
        #serializer_class = GroupSerializer
        return views.objects.all()
#@api_view(['GET','POST'])
#def getlist(request,format=None):
#    if request.method == 'GET':
 #       meizis = User.objects.all()



def yc_create(request):
    post=request.POST
    print(post)
    gtitle=post.get('title')
    gcontext=post.get('context')
    print(gcontext)
    gpic=request.FILES['pic']
    print(gpic)
    user=views()
    #s1=sha1()
    #s1.update(gtitle.encode("utf-8"))
    #ztitle=s1.hexdigest()
    #print("-----%s------"%ztitle)
    #user.gtitle=ztitle
    user.gtitle=gtitle.encode("utf-8")
    user.gcontext=gcontext
    user.gpic=gpic
    #user.gpic=gpic
    print("---1-----")
    user.save()
    print("---2-----")
    return redirect('/list')



def yc_sumbit(request):
    return render(request,'submit_list.html')


def  yc_list(request):
    ##
    list_page=views.objects.filter()
    return render(request, 'list.html', {'list_page':list_page})
    ##
