from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoview(request):
    all_items = TodoItem.objects.all()
    return render(request,'todo.html',{'allitem': all_items})

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')   

def deleteTodo(request, todo_id):
    item_del = TodoItem.objects.get(id = todo_id)
    item_del.delete()
    return HttpResponseRedirect('/todo/')    


