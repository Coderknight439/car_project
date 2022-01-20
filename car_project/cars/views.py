from .forms import CarForm
from django.shortcuts import render, redirect
from .tables import CarsTable
from django.contrib import messages
from .models import Cars
from django.contrib.auth.decorators import login_required


@login_required
def create_car(request, **kwargs):
    form = CarForm(request.POST or None)
    if form.is_valid():
        try:
            form.save()
            messages.success(request, "Car Created Successfully")
            return redirect('car_index')
        except Exception as e:
            print(e)
            messages.error(request, message="Car Couldn't be created.")
    return render(request, 'cars/create.html', {'form': form, 'title': 'Create Car'})


@login_required
def index(request):
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('per_page', 15))
    table = CarsTable(Cars.objects.all())
    table.paginate(page=page, per_page=page_size)
    return render(request, 'cars/list.html', {'table': table, 'title': 'Car List'})


@login_required
def edit(request, car_id, **kwargs):
    data_obj = Cars.objects.get(pk=car_id)
    form = CarForm(instance=data_obj)
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Car Updated Successfully")
                return redirect('car_index')
            except Exception as e:
                print(e)
                messages.success(request, message="Update Error")
    return render(request, 'cars/create.html', {'form': form, 'title': 'Edit Car'})


@login_required
def delete(request, car_id, **kwargs):
    if request.method == 'POST':
        try:
            obj = Cars.objects.get(pk=car_id)
            obj.delete()
            messages.success(request, "Car Deleted Successfully")
            return redirect('car_index')
        except Exception as e:
            print(e)
            pass
    car_name = request.GET.get('car_name')
    return render(request, 'cars/delete_confirm.html', {'car_name': car_name, 'title': 'Delete Car'})
