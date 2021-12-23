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
  types = request.GET['types'].split(',')
  bound_lower = request.GET['bound_lower'].split(',')
  bound_upper = request.GET['bound_upper'].split(',')
  radius = int(request.GET.get('radius', '50000'))
  all_places = int(request.GET.get('all_places', '0'))

  bound_lower = [float(b) for b in bound_lower]
  bound_upper = [float(b) for b in bound_upper]

  ret = populartimes.get(
    settings.MAPS_API_KEY,
    types,
    bound_lower,
    bound_upper,
    n_threads=20,
    radius=radius,
    all_places=all_places,
  )
  return http.JsonResponse({'results': ret})
