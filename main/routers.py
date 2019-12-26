from rest_framework.routers import DefaultRouter


from restapp.apiviews import (
    BookViewSet,
    AuthorViewSet
)

router = DefaultRouter()

router.register('author' , AuthorViewSet,basename='author')
router.register('book' , BookViewSet , basename='book')


urlpatterns = router.urls
