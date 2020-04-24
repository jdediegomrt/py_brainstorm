import logging
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_GET

from .remote_apis import opentdb_api_client

import utils

logger = logging.getLogger(__name__)


@require_GET
def trivia_game_questions(request):
    try:
        utils.verify_request_contains_required_parameters(request, 'amount', 'category')
    except Exception as ex:
        return HttpResponseBadRequest(ex)
    return JsonResponse(opentdb_api_client.trivia_game_questions(request.GET['amount'], request.GET['category']))


@require_GET
def trivia_game_categories(request):
    return JsonResponse(opentdb_api_client.trivia_game_categories())
