from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Property
from .serializers import PropertyListSerializer, PropertyDetailSerializer


class PropertyPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = "page_size"
    max_page_size = 50


class PropertyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Property.objects.filter(is_active=True)
    pagination_class = PropertyPagination

    def get_serializer_class(self):
        if self.action == "list":
            return PropertyListSerializer
        return PropertyDetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params

        # Location filter
        location = params.get("location")
        if location:
            queryset = queryset.filter(location__icontains=location)

        # Price range filter
        price_min = params.get("price_min")
        price_max = params.get("price_max")
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)

        # Property type filter
        property_type = params.get("property_type")
        if property_type:
            queryset = queryset.filter(property_type=property_type)

        # Sorting
        sort = params.get("sort", "most_recent")
        sort_mapping = {
            "most_recent": "-created_at",
            "price_asc": "price",
            "price_desc": "-price",
            "area_asc": "area",
            "area_desc": "-area",
        }
        order_by = sort_mapping.get(sort, "-created_at")
        return queryset.order_by(order_by)
