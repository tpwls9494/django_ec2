from django.urls import path
from .views import hello_view

urlpatterns = [
<<<<<<< Updated upstream
    path('', hello_view)
=======
    path('hello/', hello_view, name='hello_view'),
>>>>>>> Stashed changes
]
