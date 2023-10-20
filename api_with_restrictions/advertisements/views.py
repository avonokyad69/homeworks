from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permission import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        print(self.request.user)
        if self.request.user.is_authenticated == True:
            return Advertisement.objects.all().filter(creator=self.request.user) | Advertisement.objects.all().exclude(status='DRAFT')
        return Advertisement.objects.all().exclude(status='DRAFT')


    def get_permissions(self):
        """Получение прав для действий."""

        if self.action in ["create", "update", "partial_update", "destroy"]:
            if self.request.user.is_staff == False:
                return [IsAuthenticated(), IsOwnerOrReadOnly()]
            else:
                return [IsAuthenticated()]
        return []
