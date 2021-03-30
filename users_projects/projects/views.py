from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Projects
from .forms import ProjectForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.template import loader 
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

class IndexClassView(ListView):
    model = Projects
    template_name = 'projects/index.html'
    paginate_by = 3
    context_object_name = 'project_list'

def listing(request):
    contact_list = Projects.objects.all()
    paginator = Paginator(contact_list, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'projects/index.html', {'page_obj': page_obj})

# def post_list(request):
#     object_list = Projects.objects.all()

#     paginator = Paginator(object_list, 3) #3 posts in each page
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'projects/index.html', {'page':page, 'posts':posts})

class ProjectDetail(DetailView):
    model = Projects
    template_name = 'projects/detail.html'

class CreateProject(CreateView):
    model = Projects
    fields = ['project_name','project_desc', 'project_image']
    template_name = 'projects/project-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

def update_item(request,id):
    item = Projects.objects.get(id = id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('projects:index')
    return render(request, 'projects/project-form.html',{'form' : form,'item' : item})

def delete_item(request,id):
    item = Projects.objects.get(id = id)
    import pdb; pdb.set_trace()
    if request.method == 'POST':
        item.delete()
        return redirect('projects:index')
    return render(request, 'projects/project-delete.html',{'item' : item})

def view_item(request):
    current_user = request.user
    item = Projects.objects.filter(user_name=current_user.id)
    return render(request, 'projects/projects.html', {'item': item})
