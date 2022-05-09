from unicodedata import category, name
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Garment, Outfit
from .forms import GarmentForm, OutfitForm

# Create your views here.
@login_required(login_url='/login')
def wardrobe(request):
    latest_garment_list = Garment.objects.select_related().filter(user=request.user).order_by('-date')
    latest_outfit_list = Outfit.objects.select_related().filter(user=request.user).order_by('-date')

    context = {
        'latest_garment_list': latest_garment_list,
        'latest_outfit_list': latest_outfit_list,
        'nbar': 'wardrobe',
    }
    
    return render(request, 'wardrobe/wardrobe.html', context)

@login_required(login_url='/login')
def garment_upload(request):
    if request.method == 'POST':
        form = GarmentForm(request.POST, request.FILES)
        if form.is_valid():
            garment = form.save(commit=False)
            garment.user = request.user
            garment.save()
            form.save_m2m()
            return redirect('wardrobe:wardrobe')
    else:
        form = GarmentForm()
    return render(request, 'wardrobe/garment_form.html', {'form': form})

@login_required(login_url='/login')
def garment_detail(request, garment_id):
    garment = get_object_or_404(Garment, pk=garment_id)
    return render(request, 'wardrobe/garment_detail.html', {'garment': garment})

@login_required(login_url='/login')
def garment_edit(request, garment_id):
    record = get_object_or_404(Garment, user=request.user, pk=garment_id)
    if request.method == 'POST':
        form = GarmentForm(request.POST, files=request.FILES, instance=record)
        if form.is_valid():
            form.save()
            return redirect('wardrobe:garment_detail', garment_id=garment_id)
    else:
        form = GarmentForm(instance=record)
    return render(request, 'wardrobe/garment_edit.html', {'form': form, 'garment_id': garment_id})

@login_required(login_url='/login')
def garment_delete(request, garment_id):
    record = get_object_or_404(Garment, user=request.user, pk=garment_id)
    if request.method == 'POST':
        record.delete()
    return redirect('wardrobe:wardrobe')

@login_required(login_url='/login')
def outfit_create(request):
    if request.method == 'POST':
        form = OutfitForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            outfit = form.save(commit=False)
            outfit.user = request.user
            outfit.save()
            form.save_m2m()
            return redirect('wardrobe:wardrobe')
    else:
        form = OutfitForm(request=request)
    return render(request, 'wardrobe/outfit_form.html', {'form': form})

@login_required(login_url='/login')
def outfit_detail(request, outfit_id):
    outfit = get_object_or_404(Outfit, pk=outfit_id)
    return render(request, 'wardrobe/outfit_detail.html', {'outfit': outfit})

@login_required(login_url='/login')
def outfit_edit(request, outfit_id):
    record = get_object_or_404(Outfit, user=request.user, pk=outfit_id)
    if request.method == 'POST':
        form = OutfitForm(request.POST, files=request.FILES, instance=record, request=request)
        if form.is_valid():
            form.save()
            return redirect('wardrobe:outfit_detail', outfit_id=outfit_id)
    else:
        form = OutfitForm(instance=record, request=request)
    return render(request, 'wardrobe/outfit_edit.html', {'form': form, 'outfit_id': outfit_id})

@login_required(login_url='/login')
def outfit_delete(request, outfit_id):
    record = get_object_or_404(Outfit, user=request.user, pk=outfit_id)
    if request.method == 'POST':
        record.delete()
    return redirect('wardrobe:wardrobe')