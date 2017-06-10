from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import *
from .forms import *
# Create your views here.


def posts_user(request):
	if request.user.is_authenticated():
		context = {
			"title":"User is authenticated"
		}
	else:
		context = {
			"title":"User is not authenticated"
		}
	return render(request, 'index.html', context)


def posts_create(request):
	form = Postform(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "created Successfully")
		return redirect('posts_list')
		print (form.cleaned_data.get("Title"))
		print (form.cleaned_data.get("Content"))
	else:
		messages.error(request, "Not created Successfully")
	context = {
		"form":form,
		"title": 'Create',
	}
	return render(request, 'post-form.html', context)

def posts_detail(request, id):
	instance = get_object_or_404(Post, id=id)
	context = {
		"instance":instance,
		"title":instance.Title,
	}
	return render(request, 'post_details.html', context)


def posts_list(request):
	queryset_list = Post.objects.filter(Draft=False).filter(Publish__lte=timezone.now())#all() #.order_by("-Timestamp")
	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"post_list": queryset,
		"title":"List"
	}
	return render(request, 'post_list.html', context)



def posts_update(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	form = Postform(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Updated Successfully")
		return redirect('posts_list')
	else:
		messages.error(request, " Not updated Successfully")
	context = {
		"Title": instance.Title,
		"instance": instance,
		"form":form,
	}	
	return render(request, 'post-form.html', context)

def posts_delete(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	print(instance)
	messages.success(request, "Deleted Successfully")
	return redirect('posts_list')