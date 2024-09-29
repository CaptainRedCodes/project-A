from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from item.models import Item
from .forms import EditItemForm, NewItemForm

# Create your views here.
def detail(request,pk):
    item=get_object_or_404(Item,pk=pk)

    return render(request,'item/detail.html',{'item':item})

@login_required
def new(request):
    if(request.method=='POST'):
        form=NewItemForm(request.POST,request.FILES)

        if form.is_valid():
            item=form.save(commit=False) # as item doesnt have created by field while adding, we add that field here and save it to db else it will show error
            item.created_by=request.user
            item.save()

            return redirect('item:detail',pk=item.id)
    else:
        form=NewItemForm()

    return render(request,'item/form.html',{
        'form':form,
        'title':'New item'
    })


@login_required
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()


    return redirect('dashboard:index')


@login_required
def edit(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    if(request.method=='POST'):
        form=EditItemForm(request.POST,request.FILES,instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail',pk=item.id)
    else:
        form=EditItemForm(instance=item)

    return render(request,'item/form.html',{
        'form':form,
        'title':'Edit item'
    })