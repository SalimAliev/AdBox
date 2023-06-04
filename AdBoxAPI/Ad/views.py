import json

from django.core.paginator import Paginator
from django.db.models import Prefetch
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Ad, AdPhoto
from rest_framework.views import APIView


class AdAPIView(APIView):
    def get(self, request, ad_id=None):
        if ad_id is None:
            order_field = request.GET.get('order', 'price,data_create').split(',')
            ad_data = Ad.objects.prefetch_related(Prefetch('photos', queryset=AdPhoto.objects.all(), to_attr='first_photo')).only('title', 'price').order_by(*order_field)

            paginator = Paginator(ad_data, 2)
            page_number = request.GET.get('page', 1)
            ad_data = paginator.get_page(page_number)

            ad_list = []
            for ad in ad_data:
                ad_dict = {
                    'title': ad.title,
                    'price': ad.price,
                    'image_path': [path.image_path for path in ad.first_photo][0] if len(ad.first_photo) != 0 else None
                }
                ad_list.append(ad_dict)
            return Response({'page': page_number, 'page_count': paginator.count, 'response': ad_list})
        else:
            ad_data = Ad.objects.get(pk=ad_id)

            image_path = [path.image_path for path in AdPhoto.objects.filter(advertisement=ad_id)]
            response = {
                'title': ad_data.title,
                'price': ad_data.price,
            }

            fields = request.GET.get('fields', None)
            if fields:
                if 'photos' in fields:
                    response['image_path'] = image_path
                else:
                    response['image_path'] = image_path[0]

                if 'description' in fields:
                    response['description'] = ad_data.description

            return Response({'response': response})

    def post(self, request):
        ad_new = Ad.objects.create(
            title=request.data['title'],
            price=request.data['price'],
            description=request.data['description']
        )

        image_paths = request.data['image_paths']
        if len(image_paths) > 3:
            return JsonResponse({'response': 'Error, the number of photos should not exceed 3'})

        ad_photos = [
            AdPhoto(advertisement=ad_new, image_path=path)
            for path in image_paths
        ]
        AdPhoto.objects.bulk_create(ad_photos)
        return JsonResponse({'status': 'success:', 'id': ad_new.id})