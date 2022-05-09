from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from .forms import NewUserForm, UserProfileForm, MessageForm
from .models import UserProfile, Message
from wardrobe.models import Garment, Outfit

# Create your views here.
def homepage(request):
	top_profiles = UserProfile.objects.annotate(f_count=Count('followers')) \
                                .order_by('-f_count')[:3]
	context = {
		'top_profiles':top_profiles,
		'nbar': 'home',
	}

	return render(request, 'core/homepage.html', context)

@login_required(login_url='/login')
def feed(request):
	following = UserProfile.objects.filter(followers__username=request.user).values_list('user', flat=True)
	outfits = Outfit.objects.filter(user__in=following).order_by('-date')

	top_profiles = UserProfile.objects.annotate(f_count=Count('followers')) \
                                .order_by('-f_count')[:4]

	context = {
		'outfits': outfits,
		'top_profiles': top_profiles,
		'nbar': 'feed',
	}

	return render(request, 'core/feed.html', context)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			UserProfile(user=user).save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("core:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="core/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("core:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="core/login.html", context={"login_form":form})

@login_required(login_url='/login')
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("core:homepage")

@login_required(login_url='/login')
def edit_profile(request):
	record = get_object_or_404(UserProfile, user=request.user)
	if request.method == 'POST':
		form = UserProfileForm(request.POST, files=request.FILES, instance=record)
		if form.is_valid():
			form.save()
			return redirect('core:user_profile', username=request.user.username)
	else:
		form = UserProfileForm(instance=record)
	return render(request, 'core/user_profile_form.html', {'form': form})

def search_results(request):
	if request.method == "POST":
		searched = request.POST['searched']
		profiles = UserProfile.objects.filter(user__username__contains=searched, private=False)
		return render(request, 'core/search_results.html', {'searched':searched, 'profiles':profiles})
	else:
		return render(request, 'core/search_results.html', {})

def top_profiles_list(request):
	top_profiles = UserProfile.objects.annotate(f_count=Count('followers')) \
                                .order_by('-f_count')
	return render(request, 'core/top_profiles_page.html', {'top_profiles':top_profiles})

def profile(request, username):
	user = get_object_or_404(User, username=username)
	profile = get_object_or_404(UserProfile, user=user)
	latest_garment_list = Garment.objects.select_related().filter(user=user).order_by('-date')
	latest_outfit_list = Outfit.objects.select_related().filter(user=user).order_by('-date')
	
	followers = profile.followers.all()

	is_following = False

	for follower in followers:
		if follower == request.user:
			is_following = True
			break

	number_of_followers = len(followers)

	context = {
		'profile': profile,
		'latest_garment_list': latest_garment_list,
		'latest_outfit_list': latest_outfit_list,
		'number_of_followers': number_of_followers,
		'is_following': is_following,
	}

	return render(request, 'core/profile.html', context)

def profile_garment_detail(request, username, garment_id):
    garment = get_object_or_404(Garment, pk=garment_id)
    return render(request, 'core/profile_garment_detail.html', {'garment': garment})

def profile_outfit_detail(request, username, outfit_id):
    outfit = get_object_or_404(Outfit, pk=outfit_id)
    return render(request, 'core/profile_outfit_detail.html', {'outfit': outfit})

@login_required(login_url='/login')
def add_follower(request, username):
	if request.method == 'POST':
		user = get_object_or_404(User, username=username)
		profile = get_object_or_404(UserProfile, user=user)
		profile.followers.add(request.user)
	return redirect('core:user_profile', username=username)

@login_required(login_url='/login')
def remove_follower(request, username):
	if request.method == 'POST':
		user = get_object_or_404(User, username=username)
		profile = get_object_or_404(UserProfile, user=user)
		profile.followers.remove(request.user)
	return redirect('core:user_profile', username=username)

@login_required(login_url='/login')
def send_message(request, username):
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			form.sender_user = request.user
			form.receiver_user = username
			form.save()
			return redirect('core:homepage')
	else:
		form = MessageForm()
	return render(request, 'core/send_message_form.html', {'form': form, 'to_user': username})

@login_required(login_url='/login')
def inbox(request):
	latest_messages = Message.objects.filter(receiver_user=request.user).order_by('-date')
	return render(request, 'core/inbox.html', {'latest_messages': latest_messages})

@login_required(login_url='/login')
def sent(request):
	latest_sent = Message.objects.filter(sender_user=request.user).order_by('-date')
	return render(request, 'core/sent.html', {'latest_sent': latest_sent})

@login_required(login_url='/login')
def inbox_detail(request, message_id):
	msg = Message.objects.get(pk=message_id)
	msg.is_read = True
	msg.save()
	return render(request, 'core/inbox_detail.html', {'msg': msg})

@login_required(login_url='/login')
def sent_detail(request, message_id):
	msg = get_object_or_404(Message, pk=message_id)
	return render(request, 'core/sent_detail.html', {'msg': msg})