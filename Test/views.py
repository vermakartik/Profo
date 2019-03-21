from django.shortcuts import render
from .models import Test
from django.http import JsonResponse
# Create your views here.
def new_test(request):
    if request.method == "POST":
        if 'test_name' in request.POST:
            test = Test(test_name=request.POST.get(test_name))
            test.save()
        return JSONResponse({'test': test, 'status': 'Success'})
    else:
        return render(request, 'Test/new_test.html')
