from django.urls import path
from .views import BlogDetail, BlogList

urlpatterns = [
    path('blog/', BlogList.as_view()), # 클래스형 뷰를 작성했기 때문에 BlogList.as_view()
    path('blog/<int:pk>', BlogDetail.as_view()),
]