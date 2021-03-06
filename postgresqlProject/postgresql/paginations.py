from rest_framework.pagination import PageNumberPagination, CursorPagination
from rest_framework.response import Response


class MyPageNumberPagination(PageNumberPagination):
    page_size = 2


class MyCursorPagination(CursorPagination):
    page_size = 2
    ordering = 'id'


class CustomPagination(PageNumberPagination):
    page = 1
    page_size = 2
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })