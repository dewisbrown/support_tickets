from rest_framework.routers import DefaultRouter


from tickets.viewsets import TicketViewSet, TicketGenericViewSet

router = DefaultRouter()
router.register('tickets', TicketGenericViewSet, basename='tickets')

urlpatterns = router.urls
