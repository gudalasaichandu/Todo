from django.shortcuts import render , redirect
from .models import Todo
# Create your views here.
def index(request):
    task=Todo.objects.all()
    if request.method=='POST':
        todo= Todo(
            Title=request.POST['matter']
        )
        todo.save()
        return redirect('/')
    return render(request,'index.html',context={'tasks':task})

def delete(request,pk):
    task1=Todo.objects.get(id=pk)

    task1.delete()
    return redirect('/')