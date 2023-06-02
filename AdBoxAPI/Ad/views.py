from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Ad

# Create your views here.


def Ad_View_List(request):
    if request.method == 'GET':
        Ads = Ad.objects.prefetch_related('photos').only('title', 'price')
        paginator = Paginator(Ads, 10)
        page_number = request.GET.get('page')
        Ads_data = paginator.get_page(page_number)
        Ads_list = []
        for ad in Ads_data:
            image_paths = [path.image_path for path in ad.photos.all()]
            Ads_dict = {
                'title': ad.title,
                'image_path': image_paths[0] if image_paths else None,
                'price': ad.price,
            }
            Ads_list.append(Ads_dict)
        return JsonResponse({'response': Ads_list})


def Ad_View(request, pk):
    if request.method == 'GET' and pk:
        Ad_data = Ad.objects.prefetch_related('photos').get(pk=pk)
        Ad_dict = {
            'title': Ad.title,
            'price': Ad.price,
            'image_path': Ad.
        }

        return JsonResponse({'response': Ads})





