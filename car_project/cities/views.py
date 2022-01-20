import json

from django.http import FileResponse, HttpResponse

from .forms import CityForm, CityUpdateForm, CityCarForm
from django.shortcuts import render, redirect
from .tables import CityTable, CityCarTable
from django.contrib import messages
from .models import Cities, CityCars
import random
import math
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from tasks.tasks import download_file


def generate_random_code():
    """
    
    :return: Return a 6 digit random code. This is very simple just for
    test
    """
    digits = [i for i in range(0, 10)]
    
    random_str = ""
    for i in range(6):
        val = math.floor(random.random() * 10)
        random_str += str(digits[val])
    
    return random_str
        

@login_required
def create_city(request, **kwargs):
    if request.method == 'POST':
        form = CityForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "city Created Successfully")
                return redirect('city_index')
            except Exception as e:
                print(e)
                messages.error(request, message="city Couldn't be created.")
                return render(request, 'cities/create.html', {'form': form, 'title': 'Create city'})
    else:
        form = CityForm()
    return render(request, 'cities/create.html', {'form': form, 'title': 'Create city'})


@login_required
def city_car_create(request, city_id, **kwargs):
    try:
        city_obj = Cities.objects.get(id=city_id)
        if request.method == 'POST':
            form = CityCarForm(request.POST)
            if form.is_valid():
                try:
                    model = form.save(commit=False)
                    if model.operator and not model.operator.code:
                        code = generate_random_code()
                        model.operator.code = code
                        
                        # Creating Operator User
                        user = User.objects.create_user(
                                username=code,
                                email=code,
                                password=code,
                                is_superuser=False,
                                is_staff=True
                        )
                        model.operator.user = user
                        model.operator.save()
                        messages.success(request, "Car Assigned Successfully")
                        return redirect('city_index')
                    else:
                        messages.success(request, "Operator Already Assigned")
                        return redirect('city_index')
                except Exception as e:
                    print(e)
                    messages.error(request, message="city Couldn't be created.")
                    return render(request, 'cities/create.html', {'form': form, 'title': 'Create city'})
        else:
            form = CityCarForm(initial={'city': city_obj})
    except Cities.DoesNotExist:
        return redirect('city_index')
    return render(request, 'cities/create.html', {'form': form, 'title': 'Assign Car'})


@login_required
def index(request):
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('per_page', 15))
    table = CityTable(Cities.objects.all())
    table.paginate(page=page, per_page=page_size)
    return render(request, 'cities/list.html', {'table': table, 'title': 'city List'})


@login_required
def city_car_index(request):
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('per_page', 15))
    table = CityCarTable(CityCars.objects.all())
    table.paginate(page=page, per_page=page_size)
    return render(request, 'cities/city_car_list.html', {'table': table, 'title': 'city List'})


@login_required
def edit(request, city_id, **kwargs):
    data_obj = Cities.objects.get(id=city_id)
    form = CityUpdateForm(instance=data_obj)
    if request.method == 'POST':
        form = CityUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "city Updated Successfully")
                return redirect('city_index')
            except Exception as e:
                print(e)
                messages.success(request, message="Update Error")
    return render(request, 'cities/create.html', {'form': form, 'title': 'Edit city', 'edit': True})


@login_required
def delete(request, city_id, **kwargs):
    if request.method == 'POST':
        try:
            obj = Cities.objects.get(pk=city_id)
            obj.delete()
            messages.success(request, "City Deleted Successfully")
            return redirect('city_index')
        except Exception as e:
            print(e)
            pass
    city_name = request.GET.get('city_name')
    return render(request, 'cities/delete_confirm.html', {'city_name': city_name, 'title': 'Delete City'})


def download_city_file(request, city_id, **kwargs):
    task_id = request.GET.get("task_id")
    if request.is_ajax():
        result = download_file.AsyncResult(task_id)
        if result.ready():
            obj = Cities.objects.get(id=city_id)
            filename = obj.model_attribute_name.path
            response = FileResponse(open(filename, 'rb'))
            return response
        return HttpResponse(json.dumps({"filename": None}))
    return HttpResponse(json.dumps({"filename": None}))
