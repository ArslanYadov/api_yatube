from rest_framework.pagination import LimitOffsetPagination

from yatube_api.settings import AMOUNT_OBJECTS_PER_PAGE


class PostPagination(LimitOffsetPagination):
    limit_query_description = AMOUNT_OBJECTS_PER_PAGE
