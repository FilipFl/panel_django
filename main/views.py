import datetime
import itertools
from main.forms import MyForm

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def basic_view(request):
    #return render(request, 'about_me.html')
    return HttpResponse('Nothing to see here...')

def prezent_view(request):
    return render(request, 'prezent2.html')

def ready_view(request):
    new_day = datetime.datetime(2021, 8, 20, 22, 00, tzinfo=None)
    if datetime.datetime.now() < new_day:
        return render(request, 'oszust.html')
    return render(request, 'prezent_lokacja.html')

def time_now(request):
    new_day = datetime.datetime(2021, 8, 19, 15, 30, tzinfo=None)

    return HttpResponse(str(datetime.datetime.now() > new_day))
    #return render(request, 'prezent2.html')

def find_sum_parts(request):
    data = {}
    result = []
    if "GET" == request.method:
        return render(request, "upload_csv.html", data)
    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            return render(request, "upload_csv.html", data)
        #if file is too large, return
        if csv_file.multiple_chunks():
            return render(request, "upload_csv.html", data)
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        sum_to_check = 0.0
        index = 0
        list_of_parts = []
        for line in lines:
            fields = line.split(",")
            if index == 0:
                sum_to_check = float(fields[1])
                index += 1
            try:
                number = float(fields[0])
                list_of_parts.append(number)
            except:
                pass
        result = [seq for i in range(len(list_of_parts), 0, -1) for seq in itertools.combinations(list_of_parts, i) if sum(seq) == sum_to_check]
    except Exception as e:
        pass
    result_dict = {'possibilities': []}
    for tup in result:
        result_dict['possibilities'].append([number for number in tup])
    return JsonResponse(result_dict, status=200)


def find_sum_parts_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        form.is_valid()
        values, sum_to_check = form.get_data()
        result = set([tuple(sorted(seq)) for i in range(len(values), 0, -1) for seq in itertools.combinations(values, i) if
                  sum(seq) == sum_to_check])
        return render(request, "result.html", {'results': result})

    else:
        form = MyForm()
    return render(request, "dynamic_form.html", {'form': form})
