from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewUserForm, UserProfileForm
from .models import UserProfile
from wardrobe.models import Garment, Outfit

# Create your views here.
def homepage(request):
    return render(request, 'core/homepage.html')

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

def edit_profile(request):
    record = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('core:user_profile', username=request.user.username)
    return render(request, 'core/user_profile_form.html', {'form': form})

def search_results(request):
	if request.method == "POST":
		searched = request.POST['searched']
		users = UserProfile.objects.filter(user__username__contains=searched, private=False)
		return render(request, 'core/search_results.html', {'searched':searched, 'users':users})
	else:
		return render(request, 'core/search_results.html', {})

def profile(request, username):
	user = get_object_or_404(User, username=username)
	profile = get_object_or_404(UserProfile, user=user)
	latest_outfit_list = Outfit.objects.select_related().filter(user=user).order_by('-date')
	tops = Garment.objects.select_related().filter(user=user, category='Top').order_by('-date')
	bottoms = Garment.objects.select_related().filter(user=user, category='Bottom').order_by('-date')
	outerwear = Garment.objects.select_related().filter(user=user, category='Outerwear').order_by('-date')
	footwear = Garment.objects.select_related().filter(user=user, category='Footwear').order_by('-date')
	accessories = Garment.objects.select_related().filter(user=user, category='Accessory').order_by('-date')
	context = {	'profile': profile,
				'latest_outfit_list': latest_outfit_list,
                'tops': tops,
                'bottoms': bottoms,
                'outerwear': outerwear,
                'footwear': footwear,
                'accessories': accessories                  }
	return render(request, 'core/profile.html', context)

def profile_garment_detail(request, username, garment_id):
    garment = get_object_or_404(Garment, pk=garment_id)
    return render(request, 'core/profile_garment_detail.html', {'garment': garment})

def profile_outfit_detail(request, username, outfit_id):
    outfit = get_object_or_404(Outfit, pk=outfit_id)
    tops = outfit.garments.filter(category='Top')
    bottoms = outfit.garments.filter(category='Bottom')
    outerwear = outfit.garments.filter(category='Outerwear')
    footwear = outfit.garments.filter(category='Footwear')
    accessories = outfit.garments.filter(category='Accessory')
    context = { 'outfit': outfit,
                'tops': tops,
                'bottoms': bottoms,
                'outerwear': outerwear,
                'footwear': footwear,
                'accessories': accessories }
    return render(request, 'core/profile_outfit_detail.html', context)
