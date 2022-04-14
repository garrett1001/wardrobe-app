from unicodedata import category, name
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Garment, Outfit
from .forms import GarmentForm, OutfitForm

# Create your views here.
@login_required(login_url='/login')
def wardrobe(request):
    # latest_garment_list = Garment.objects.select_related().filter(user=request.user).order_by('-date')
    latest_outfit_list = Outfit.objects.select_related().filter(user=request.user).order_by('-date')
    tops = Garment.objects.select_related().filter(user=request.user, category='Top').order_by('-date')
    bottoms = Garment.objects.select_related().filter(user=request.user, category='Bottom').order_by('-date')
    outerwear = Garment.objects.select_related().filter(user=request.user, category='Outerwear').order_by('-date')
    footwear = Garment.objects.select_related().filter(user=request.user, category='Footwear').order_by('-date')
    accessories = Garment.objects.select_related().filter(user=request.user, category='Accessory').order_by('-date')
    context = { #'latest_garment_list': latest_garment_list,
                'latest_outfit_list': latest_outfit_list,
                'tops': tops,
                'bottoms': bottoms,
                'outerwear': outerwear,
                'footwear': footwear,
                'accessories': accessories                  }
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
    form = GarmentForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('wardrobe:garment_detail', garment_id=garment_id)
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
        form = OutfitForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            outfit = form.save(commit=False)
            outfit.user = request.user
            outfit.save()
            form.save_m2m()
            return redirect('wardrobe:wardrobe')
    else:
        form = OutfitForm(user=request.user)
    return render(request, 'wardrobe/outfit_form.html', {'form': form})

@login_required(login_url='/login')
def outfit_detail(request, outfit_id):
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
    return render(request, 'wardrobe/outfit_detail.html', context)

@login_required(login_url='/login')
def outfit_edit(request, outfit_id):
    record = get_object_or_404(Outfit, user=request.user, pk=outfit_id)
    form = OutfitForm(request.POST or None, instance=record, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('wardrobe:outfit_detail', outfit_id=outfit_id)
    return render(request, 'wardrobe/outfit_edit.html', {'form': form, 'outfit_id': outfit_id})

@login_required(login_url='/login')
def outfit_delete(request, outfit_id):
    record = get_object_or_404(Outfit, user=request.user, pk=outfit_id)
    if request.method == 'POST':
        record.delete()
    return redirect('wardrobe:wardrobe')