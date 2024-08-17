from django.shortcuts import render
from django.http import JsonResponse
import json
# from .models import Document
from health_ir.IR_Models.Main import mainQuerySearch
from django.views.decorators.csrf import csrf_exempt
from health_ir.IR_Models.findPR import findPR


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        # documents = Document.objects.all().values_list('document', flat=True)
        print(query);
        searchResult = mainQuerySearch(query)
        # print(searchResult)
        return JsonResponse({'data': searchResult})
    return JsonResponse({'error': 'Invalid request'})


@csrf_exempt
def showPR_curve(request):
    if request.method == 'POST':
        print('i got it')
        
        JSON_string = request.POST.get('relevance')  # Retrieve the relevance data from POST request
        print(JSON_string)
        print(type(JSON_string))
        
        python_obj_dic = json.loads(JSON_string)
        print(type(python_obj_dic))
        print(python_obj_dic)
        # Pass the relevance data to the findPR function
        findPR(python_obj_dic)
        return JsonResponse({'data': 'success'})  # Return a success response or your specific data
        
    return JsonResponse({'error': 'failed'})  # Return failure response if not a POST request
