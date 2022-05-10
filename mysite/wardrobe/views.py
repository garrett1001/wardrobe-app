from unicodedata import category, name
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Outfit, Top, Bottom, Outerwear, Footwear, Accessory
from .forms import OutfitForm, TopForm, BottomForm, OuterwearForm, FootwearForm, AccessoryForm

# Create your views here.
@login_required(login_url='/login')
def wardrobe(request):
    top_list = Top.objects.select_related().filter(user=request.user).order_by('-date')
    bottom_list = Bottom.objects.select_related().filter(user=request.user).order_by('-date')
    outerwear_list = Outerwear.objects.select_related().filter(user=request.user).order_by('-date')
    footwear_list = Footwear.objects.select_related().filter(user=request.user).order_by('-date')
    accessory_list = Accessory.objects.select_related().filter(user=request.user).order_by('-date')
    outfit_list = Outfit.objects.select_related().filter(user=request.user).order_by('-date')

    context = {
        'top_list': top_list,
        'bottom_list': bottom_list,
        'outerwear_list': outerwear_list, 
        'footwear_list': footwear_list, 
        'accessory_list': accessory_list, 
        'outfit_list': outfit_list,
        'nbar': 'wardrobe',
    }
    
    return render(request, 'wardrobe/wardrobe.html', context)

# Garment Upload Functions
@login_required(login_url='/login')
def top_upload(request):
    if request.method == 'POST':
        form = TopForm(request.POST, request.FILES)
        if form.is_valid():
            garment = form.save(commit=False)
            garment.user = request.user
            garment.save()
            return redirect('wardrobe:wardrobe')
    else:
        form = TopForm()
    return render(request, 'wardrobe/garment_form.html', {'form': form, 'category': 'top'})

@login_required(login_url='/login')
def bottom_upload(request):
    if request.method == 'POST':
        form = BottomForm(request.POST, request.FILES)
        if form.is_valid():
            garment = form.save(commit=False)
            garment.user = request.user
            garment.save()
            return redirect('wardrobe:wardrobe')
    else:
        form = BottomForm()
    return render(request, 'wardrobe/garment_form.html', {'form': form, 'category': 'bottom'})

@login_required(login_url='/login')
def outerwear_upload(request):
    if request.method == 'POST':
        form = OuterwearForm(request.POST, request.FILES)
        if form.is_valid():
            garment = form.save(commit=False)
            garment.user = request.user
            garment.save()
            return redirect('wardrobe:wardrobe')
    else:
        form = OuterwearForm()
    return render(request, 'wardrobe/garment_form.html', {'form': form, 'category': 'outerwear'})

@login_required(login_url='/login')
def footwear_upload(request):
    if request.method == 'POST':
        form = FootwearForm(request.POST, request.FILES)
        if form.is_valid():
            garment = form.save(commit=False)
            garment.user = request.user
            garment.save()
            return redirect('wardrobe:wardrobe')
    else:
        form = FootwearForm()
    return render(request, 'wardrobe/garment_form.html', {'form': form, 'category': 'footwear'})

@login_required(login_url='/login')
def accessory_upload(request):
    if request.method == 'POST':
        form = AccessoryForm(request.POST, request.FILES)
        if form.is_valid():
            garment = form.save(commit=False)
            garment.user = request.user
            garment.save()
            return redirect('wardrobe:wardrobe')
    else:
        form = AccessoryForm()
    return render(request, 'wardrobe/garment_form.html', {'form': form, 'category': 'accessory'})

# Garment Detail Functions
@login_required(login_url='/login')
def top_detail(request, top_id):
    top = get_object_or_404(Top, pk=top_id)
    return render(request, 'wardrobe/garment_detail.html', {'garment': top, 'category': 'top'})

@login_required(login_url='/login')
def bottom_detail(request, bottom_id):
    bottom = get_object_or_404(Bottom, pk=bottom_id)
    return render(request, 'wardrobe/garment_detail.html', {'garment': bottom, 'category': 'bottom'})

@login_required(login_url='/login')
def outerwear_detail(request, outerwear_id):
    outerwear = get_object_or_404(Outerwear, pk=outerwear_id)
    return render(request, 'wardrobe/garment_detail.html', {'garment': outerwear, 'category': 'outerwear'})

@login_required(login_url='/login')
def footwear_detail(request, footwear_id):
    footwear = get_object_or_404(Footwear, pk=footwear_id)
    return render(request, 'wardrobe/garment_detail.html', {'garment': footwear, 'category': 'footwear'})

@login_required(login_url='/login')
def accessory_detail(request, accessory_id):
    accessory = get_object_or_404(Accessory, pk=accessory_id)
    return render(request, 'wardrobe/garment_detail.html', {'garment': accessory, 'category': 'accessory'})

# Garment Edit Functions
@login_required(login_url='/login')
def top_edit(request, top_id):
    record = get_object_or_404(Top, user=request.user, pk=top_id)
    if request.method == 'POST':
        form = TopForm(request.POST, files=request.FILES, instance=record)
        if form.is_valid():
            form.save()
            return redirect('wardrobe:top_detail', top_id)
    else:
        form = TopForm(instance=record)
    return render(request, 'wardrobe/garment_edit.html', {'form': form, 'garment_id': top_id, 'category': 'top'})

@login_required(login_url='/login')
def bottom_edit(request, bottom_id):
    record = get_object_or_404(Bottom, user=request.user, pk=bottom_id)
    if request.method == 'POST':
        form = BottomForm(request.POST, files=request.FILES, instance=record)
        if form.is_valid():
            form.save()
            return redirect('wardrobe:bottom_detail', bottom_id)
    else:
        form = BottomForm(instance=record)
    return render(request, 'wardrobe/garment_edit.html', {'form': form, 'garment_id': bottom_id, 'category': 'bottom'})

@login_required(login_url='/login')
def outerwear_edit(request, outerwear_id):
    record = get_object_or_404(Outerwear, user=request.user, pk=outerwear_id)
    if request.method == 'POST':
        form = OuterwearForm(request.POST, files=request.FILES, instance=record)
        if form.is_valid():
            form.save()
            return redirect('wardrobe:outerwear_detail', outerwear_id)
    else:
        form = OuterwearForm(instance=record)
    return render(request, 'wardrobe/garment_edit.html', {'form': form, 'garment_id': outerwear_id, 'category': 'outerwear'})

@login_required(login_url='/login')
def footwear_edit(request, footwear_id):
    record = get_object_or_404(Footwear, user=request.user, pk=footwear_id)
    if request.method == 'POST':
        form = FootwearForm(request.POST, files=request.FILES, instance=record)
        if form.is_valid():
            form.save()
            return redirect('wardrobe:footwear_detail', footwear_id)
    else:
        form = FootwearForm(instance=record)
    return render(request, 'wardrobe/garment_edit.html', {'form': form, 'garment_id': footwear_id, 'category': 'footwear'})

@login_required(login_url='/login')
def accessory_edit(request, accessory_id):
    record = get_object_or_404(Accessory, user=request.user, pk=accessory_id)
    if request.method == 'POST':
        form = AccessoryForm(request.POST, files=request.FILES, instance=record)
        if form.is_valid():
            form.save()
            return redirect('wardrobe:accessory_detail', accessory_id)
    else:
        form = AccessoryForm(instance=record)
    return render(request, 'wardrobe/garment_edit.html', {'form': form, 'garment_id': accessory_id, 'category': 'accessory'})

# Garment Delete Functions
@login_required(login_url='/login')
def top_delete(request, top_id):
    record = get_object_or_404(Top, user=request.user, pk=top_id)
    if request.method == 'POST':
        record.delete()
    return redirect('wardrobe:wardrobe')

@login_required(login_url='/login')
def bottom_delete(request, bottom_id):
    record = get_object_or_404(Bottom, user=request.user, pk=bottom_id)
    if request.method == 'POST':
        record.delete()
    return redirect('wardrobe:wardrobe')

@login_required(login_url='/login')
def outerwear_delete(request, outerwear_id):
    record = get_object_or_404(Outerwear, user=request.user, pk=outerwear_id)
    if request.method == 'POST':
        record.delete()
    return redirect('wardrobe:wardrobe')

@login_required(login_url='/login')
def footwear_delete(request, footwear_id):
    record = get_object_or_404(Footwear, user=request.user, pk=footwear_id)
    if request.method == 'POST':
        record.delete()
    return redirect('wardrobe:wardrobe')

@login_required(login_url='/login')
def accessory_delete(request, accessory_id):
    record = get_object_or_404(Accessory, user=request.user, pk=accessory_id)
    if request.method == 'POST':
        record.delete()
    return redirect('wardrobe:wardrobe')

# Outfit Functions
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