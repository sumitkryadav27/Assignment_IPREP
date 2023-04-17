from django.shortcuts import render,redirect
from django.http import HttpResponse
from main.models import Company,Employee

# Create your views here.


def companies_view(request):
    return render(request, 'companies.html', {"companies": Company.objects.all()})

def add_employee_view(request, company_id):
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        employee = Employee.objects.get(id = employee_id)
        company = Company.objects.get(id = company_id)
        employee.company = company
        employee.save()
        return redirect('api:companies')

    employees = Employee.objects.all()
    context = {
        'company_id':company_id,
        'employees':employees,
    }
    return render(request, 'add_employee.html', context)