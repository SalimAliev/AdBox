import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Ad, AdPhoto


# function of getting list of ad
def Ad_View_List(request):
    if request.method == 'GET':
        ads = Ad.objects.prefetch_related('photos').only('title', 'price')

        paginator = Paginator(ads, 10)
        page_number = request.GET.get('page')
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
        return JsonResponse({'response': ads_list})


# function of getting one ad by the passed id
def Ad_View(request, pk):
    if request.method == 'GET' and pk:
        ad_data = Ad.objects.get(pk=pk)

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
def Ad_Create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        image_paths = data.pop('image_paths', [])
        advertisement = Ad.objects.create(**data)
        for path in image_paths:
            AdPhoto.objects.create(advertisement=advertisement, image_path=path)
        return JsonResponse({'status': 'success:', 'id': advertisement.id})



