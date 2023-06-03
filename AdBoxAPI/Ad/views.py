import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Ad, AdPhoto


# function of getting list of ad
def ad_view_list(request):
    if request.method == 'GET':
        ordering = request.GET.get('ordering', 'price, data_create')
        ordering_fields = [field.strip() for field in ordering.split(',')]
        ads = Ad.objects.prefetch_related('photos').only('title', 'price').order_by(*ordering_fields)

        paginator = Paginator(ads, 2)
        page_number = request.GET.get('page', '1')
        ads_data = paginator.get_page(page_number)

        ads_list = []
        for ad in ads_data:
            image_paths = [path.image_path for path in ad.photos.all()]
            ads_dict = {
                'title': ad.title,
                'image_path': image_paths[0] if image_paths else None,
                'price': ad.price,
            }
            ads_list.append(ads_dict)

        return JsonResponse({'page': page_number, 'page_count': paginator.count, 'response': ads_list})


# function of getting one ad by the passed id
def ad_view(request, pk):
    if request.method == 'GET' and pk:
        ad_data = get_object_or_404(Ad, pk=pk)

        ad_dict = {
            'title': ad_data.title,
            'price': ad_data.price,
        }

        fields = request.GET.get('fields', None)
        ad_photos = AdPhoto.objects.filter(advertisement_id=pk)

        if fields:
            fields = fields.split(',')
            ad_dict['image_path'] = [path.image_path for path in ad_photos] if 'photos' in fields else ad_photos[0].image_path
            ad_dict['description'] = ad_data.description if 'description' in fields else None
        else:
            ad_dict['image_path'] = ad_photos[0].image_path

        return JsonResponse({'response': ad_dict})


# ad creation function
def ad_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        image_paths = data.pop('image_paths', [])
        advertisement = Ad.objects.create(**data)
        if len(image_paths) > 3:
            return JsonResponse({'response': 'Error, the number of photos should not exceed 3'})
        for path in image_paths:
            AdPhoto.objects.create(advertisement=advertisement, image_path=path)
        return JsonResponse({'status': 'success:', 'id': advertisement.id})



