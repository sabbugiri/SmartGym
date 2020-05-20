from django.shortcuts import render, HttpResponse,redirect
from django.template import loader
from django.http import HttpResponse

from .forms import GymForm

from gyms.models import *

# Create your views here.
def dashboard(request):

	template = loader.get_template('dashboard.html')
	logged_in = False
	user = ''
	profile_complete = 0
	if is_authenticated(request):
		user = request.session.get('username')
		profile_complete = request.session.get('profile_complete')
		logged_in = True
		userObj = User.objects.filter(username = user).first()
		gymObj = Gym.objects.filter(user = userObj.pk)



		context = {
				'logged_in':logged_in,
				'username' : user,
				'user' : userObj,
				'gym_count' : gymObj.count(),
				'profile_complete' : profile_complete,
				}
		return HttpResponse(template.render(context, request))
	else:
		return redirect('/login')	

def create_gym(request):
	if is_authenticated(request):
		gym_count = request.session.get('gym_count')
		if request.POST:
			gym_form = GymForm(request.POST)
			if gym_form.is_valid():
				gym = gym_form.save()
				return redirect("/gymadmin/gyms")
			else:
				template = loader.get_template('add_gym.html')
				context = {'gym_form':gym_form, 'gym_count':gym_count}
				return HttpResponse(template.render(context, request))

		gym_form = GymForm()
		template = loader.get_template('add_gym.html')
		context = {'gym_form':gym_form, 'gym_count':gym_count}
		return HttpResponse(template.render(context, request))

	else:
		return redirect('/login')	

def update_gym(request, gym_id):
	if is_authenticated(request):
		gym_count = request.session.get('gym_count')
		if request.method == "POST":
			pass

		else:	
			gym = Gym.objects.filter(pk = gym_id).first()
			gym_form = GymForm(gym)
			template = loader.get_template('gyms/edit_gym.html')
			context = {'gym_form':gym_form, 'gym_count':gym_count}
			return HttpResponse(template.render(context, request))


	else:
		return redirect('/login')		


def gyms(request):
	if is_authenticated(request):
		template = loader.get_template('gyms/home.html')
		user = request.session.get('username')
		user_id = request.session.get('user_id')
		gym_count = request.session.get('gym_count')
		gyms = Gym.objects.filter(user_id= user_id)
		context = {'gyms':gyms, 'gym_count':gym_count, 'user':user}
		return HttpResponse(template.render(context, request))

	else:
		return redirect('/login')	




def gym_details(request, gym_id):
	if is_authenticated(request):
		template = loader.get_template('gyms/details.html')
		gym_count = request.session.get('gym_count')
		user = request.session.get('username')
		gym = Gym.objects.filter(pk = gym_id).first()
		context = {'gym':gym, 'gym_count':gym_count, 'user':user}
		return HttpResponse(template.render(context, request))



	else:
		return redirect('/login')	


def gym_delete(request, gym_id):
	if is_authenticated(request):
		#template = loader.get_template('gyms/details.html')
		#gym_count = request.session.get('gym_count')
		gym = Gym.objects.filter(pk = gym_id).first()
		gym.delete()
		#context = {'gym':gym, 'gym_count':gym_count, 'user':user}
		return redirect('/gymadmin/gyms')



	else:
		return redirect('/login')	





def is_authenticated(request):
	user = request.session.get('username')
	return user
