from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    loans = Loan.objects.all()
    form = LoanForm()

    if request.method =='POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'loans':loans, 'form':form}
    return render(request, "index.html", context)

def LoanDescription(request, loan_title):
    loan = Loan.objects.get(title = loan_title)
    form = LoanForm(instance=loan)
    if request.method == 'POST':
        form = LoanForm(request.POST, instance= loan)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'loan':loan.title, 'overpayment' : loan.calculate_overpayment(), 'paid_value' : loan.calculate_paid_value(), 'monthly_instalment': loan.calculate_monthly_instalment()}
    return render(request,"loan.html",context)
