from django.shortcuts import render, redirect, HttpResponse
from .forms import DataForm
from .models import Data
import openpyxl
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    if request.method == "POST":
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Home")
    form = DataForm()
    data = Data.objects.all()
    ctx = {
        "form": form,
        "data": data,
    }
    return render(request, "excapp/index.html", context=ctx)


def detail(request, id):
    data = Data.objects.get(pk=id)
    wb = openpyxl.load_workbook(data.file)
    worksheets = wb.worksheets[0]
    excel_data = list()
    for row in worksheets.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        excel_data.append(row_data)
    context = {
        "excell": excel_data,
        "data": data,
    }
    return render(request, "excapp/detail.html", context=context)


def detail_info(request, id):
    data = Data.objects.get(pk=id)
    wb = openpyxl.load_workbook(data.file)
    worksheets = wb.worksheets[0]
    excel_data = list()
    for row in worksheets.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        excel_data.append(row_data)
    return HttpResponse(json.dumps(excel_data, ensure_ascii=False))


@csrf_exempt
def upload_info(request):
    if request.method == "POST":
        data = json.loads(request.read().decode('utf-8'))
        for i in data["data"]:
            print(i)
        return HttpResponse("ok")

    return HttpResponse("error")
