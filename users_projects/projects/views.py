from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Projects
from .forms import ProjectForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.template import loader 
# Create your views here.

class IndexClassView(ListView):
    model = Projects
    template_name = 'projects/index.html'
    context_object_name = 'project_list'

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
    # user = Projects.objects.get(id=id)
    current_user = request.user
    item = Projects.objects.filter(user_name=current_user.id)
    # print(current_user, current_user.id)
    print(item)
    return render(request, 'projects/projects.html', {'item': item})
# class SelfClassView(ListView):
#     model = Projects
#     template_name = 'projects/projects.html'
#     context_object_name = 'project_list'