from rest_framework.pagination import PageNumberPagination


class StandPagination(PageNumberPagination):
    page_size = 5