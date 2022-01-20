from .forms import PartyForm
from django.shortcuts import render, redirect
from .tables import PartiesTable
from django.contrib import messages
from .models import Parties
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def create_party(request, **kwargs):
    form = PartyForm(request.POST or None)
    if form.is_valid():
        try:
            form_data = form.cleaned_data
            party = form.save(commit=False)
            if form.cleaned_data.get('user_type') == '1':  # Manager
                user = User.objects.create_user(
                        username=form_data.get('email'),
                        email=form_data.get('email'),
                        password='1234',
                        is_superuser=True
                )  # Creating with default password
                party.user = user
                party.save()
            party.save()
            messages.success(request, "Party Created Successfully")
            return redirect('party_index')
        except Exception as e:
            print(e)
            messages.error(request, message="Party Couldn't be created.")
    return render(request, 'parties/create.html', {'form': form, 'title': 'Create Party'})


@login_required
def index(request):
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('per_page', 15))
    table = PartiesTable(Parties.objects.all())
    table.paginate(page=page, per_page=page_size)
    return render(request, 'parties/list.html', {'table': table, 'title': 'Party List'})


@login_required
def edit(request, party_id, **kwargs):
    data_obj = Parties.objects.get(pk=party_id)
    form = PartyForm(instance=data_obj)
    if request.method == 'POST':
        form = PartyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Party Updated Successfully")
                return redirect('party_index')
            except Exception as e:
                print(e)
                messages.success(request, message="Update Error")
    return render(request, 'parties/create.html', {'form': form, 'title': 'Edit Party'})


@login_required
def delete(request, party_id, **kwargs):
    if request.method == 'POST':
        try:
            obj = Parties.objects.get(pk=party_id)
            obj.delete()
            messages.success(request, "Party Deleted Successfully")
            return redirect('party_index')
        except Exception as e:
            print(e)
            pass
    party_name = request.GET.get('party_name')
    return render(request, 'parties/delete_confirm.html', {'party_name': party_name, 'title': 'Delete Party'})
