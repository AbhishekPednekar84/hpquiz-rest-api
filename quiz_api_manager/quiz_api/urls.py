from .views import BookViewSet, QuestionViewSet, AnalyticViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("books", viewset=BookViewSet, basename="book")
router.register("questions", viewset=QuestionViewSet, basename="questions-list")
router.register("questions?book_id=<int: book_id>",
                viewset=QuestionViewSet, basename="question")
# router.register("analytics", viewset=AnalyticViewSet, basename="analytics")

urlpatterns = router.urls
