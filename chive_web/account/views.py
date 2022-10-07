from django.shortcuts import redirect, render
from .forms import RegisterFrom
from django.contrib.auth import login, logout, authenticate
from rest_framework.generics import GenericAPIView
from .serializers import RegisterSerializer


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = RegisterFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            print('stupid')
    else:
        form = RegisterFrom()

    return render(request, 'registration/sign_up.html', {'form': form})


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        pass


def test(request):
    return render(request, 'account/test.html', {})
