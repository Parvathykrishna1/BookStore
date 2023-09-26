from django.db.models import Q
from django.shortcuts import render

from store.models import Book


# Create your views here.
def searchresult(request):
    query=""
    books=None
    if(request.method=="POST"):
        query=request.POST.get('q')
        if(query):
            books=Book.objects.filter(Q(name__icontains=query) | Q(author__icontains=query))
        return render(request,'searchresult.html',{'query':query,'books':books})