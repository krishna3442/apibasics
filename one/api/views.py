from rest_framework import generics,mixins
from one.models import BlogPost
from .serializers import BlogPostSerializer
from django.db.models import Q



class BlogPostApiView(mixins.CreateModelMixin,generics.ListAPIView):
    serializer_class=BlogPostSerializer

    def get_queryset(self):
        qs=BlogPost.objects.all()
        query=self.request.GET.get("q")
        if query is not None:
            qs=qs.filter(Q(title__icontains=query)).distinct()


        return qs


    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()
