from django.core.paginator import Paginator
from django.db.models import Prefetch
from django.http import JsonResponse

from .models import Ad, AdPhoto

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AdListSerializer, AdSerializer, AdCreateSerializer


class AdAPIView(APIView):
    def get(self, request, ad_id=None):
        if ad_id is None:
            order_field = request.GET.get('order', 'price,data_create').split(',')
            ad_data = Ad.objects.prefetch_related(Prefetch('photos', queryset=AdPhoto.objects.all(), to_attr='first_photo')).all().order_by(*order_field)

            paginator = Paginator(ad_data, 2)
            page_number = request.GET.get('page', 1)
            ad_data = paginator.get_page(page_number)

            data_serializer = AdListSerializer(ad_data, many=True).data
            for i in range(len(data_serializer)):
                data_serializer[i]['image_path'] = [path.image_path for path in ad_data[i].first_photo][0] if len(ad_data[i].first_photo) > 0 else None

            return Response({'page': page_number, 'page_count': paginator.count, 'response':data_serializer})

        else:
            ad_data = Ad.objects.get(pk=ad_id)

            image_path = [path.image_path for path in AdPhoto.objects.filter(advertisement=ad_id)]
            data_serializer = AdSerializer(ad_data).data

            fields = request.GET.get('fields', None)
            if fields:
                if 'photos' in fields:
                    data_serializer['image_path'] = image_path
                else:
                    data_serializer['image_path'] = image_path[0]

                if 'description' in fields:
                    data_serializer['description'] = ad_data.description
            else:
                data_serializer['image_path'] = image_path[0]

            return Response({'response': data_serializer})

    def post(self, request):
        serializer = AdCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ad_new = Ad.objects.create(
            title=request.data['title'],
            price=request.data['price'],
            description=request.data['description']
        )

        image_paths = request.data.get('image_paths', [])
        if len(image_paths) > 3:
            return JsonResponse({'response': 'Error, the number of photos should not exceed 3'})
        elif 0 >= len(image_paths):
            return JsonResponse({'image_path': 'Обязательное поле.'})

        ad_photos = [
            AdPhoto(advertisement=ad_new, image_path=path)
            for path in image_paths
        ]
        AdPhoto.objects.bulk_create(ad_photos)
        return JsonResponse({'status': 'success:', 'id': ad_new.id})