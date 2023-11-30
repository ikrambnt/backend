from django.shortcuts import render, get_object_or_404, redirect
from .models import Group
from .forms import GroupForm

def details_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    groups = Group.objects.all()
    context = {"group": group, "group_html": groups}
    return render(request, "groups/group_detail.html", context)
#creation / modification / supression d'un groupe


def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.admin = request.user
            group.save()
            form.save_m2m() 
            return redirect('groups:group_list') #ps. a chanegr redirige vers la page de détail du groupe
    else:
        form = GroupForm()

    return render(request, "groups/create_group.html", {'form': form})




# groups/views.py
from django.shortcuts import render
from .models import Group

def groups_list(request):
    groups = Group.objects.all()
    return render(request, "groups/group_list.html", {'groups': groups})


# groups/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Group
from .forms import GroupForm

def update_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            group.admin = request.user
            group.save()
            form.save_m2m()
            return redirect('groups:group_detail', group_id=group.id)
    else:
        form = GroupForm(instance=group)

    return render(request, "groups/update_group.html", {'form': form, 'group': group})



# groups/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Group

@require_POST
def delete_group(request):
    group_id = request.POST.get('group_id')
    try:
        group = get_object_or_404(Group, id=group_id)
        group.delete()
        return JsonResponse({'message': 'Group deleted successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

