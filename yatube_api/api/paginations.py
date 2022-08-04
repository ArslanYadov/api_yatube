from rest_framework.pagination import LimitOffsetPagination


class PostPagination(LimitOffsetPagination):
    limit_query_description = 5
