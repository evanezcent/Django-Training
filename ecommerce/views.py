from todoproject.response import Response
from . import transformer
from .models import Users


def index(request):
    user = Users.objects.all()
    user = transformer.transform(user)
    return Response.ok(values=user)