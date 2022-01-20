from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from parties.models import Parties
from tasks.tasks import download_file
from django.contrib.auth.decorators import login_required
from cities.models import CityCars


def sign_in(request, **kwargs):
	redirect_url = '/dashboard'
	user = None
	party = None
	if request.user.is_authenticated:
		return redirect(redirect_url)
	if request.method == 'POST':
		username = request.POST.get('username')
		party = Parties.objects.filter(code=username).first()
		if party:  # for operator login
			user = authenticate(username=username, password=username)
		else:
			user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
	if user:
		login(request, user)
		if party:
			city_car = CityCars.objects.filter(operator_id=party.id).first()
			filepath = city_car.city.city_file if city_car else ''  # Logic to get the file from
			if filepath:
				pass  # downloading file
				# task = download_file.delay(filepath)
				# return redirect(redirect_url+'?task_id='+task.id+'&city_id='+party.city_car.city.id)
		return redirect(redirect_url)
	return render(request, 'login.html')


@login_required
def sign_out(request, **kwargs):
	logout(request)
	return redirect('/')


@login_required
def dashboard(request, **kwargs):
	task_id = request.GET.get('task_id')
	city_id = request.GET.get('city_id')
	return render(request, 'home.html', {'title': 'Home', 'task_id': task_id, 'city_id': city_id})
