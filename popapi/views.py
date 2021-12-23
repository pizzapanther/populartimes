from django import http
from django.conf import settings
from django.views.decorators.cache import cache_page

import populartimes


@cache_page(60 * 15)
def get_by_id(request):
  place_id = request.GET['place_id']
  ret = populartimes.get_id(settings.MAPS_API_KEY, place_id)
  return http.JsonResponse(ret)


@cache_page(60 * 15)
def get(request):
  pass
