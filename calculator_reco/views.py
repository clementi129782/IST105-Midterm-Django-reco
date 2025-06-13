from django.shortcuts import render
from .forms import CalculatorForm
import math
import statistics

# Create your views here.
def calculate_view(request):
    result = None
    
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['input1']
            num2 = form.cleaned_data['input2']
            operator = form.cleaned_data['operator']
        
            if operator == 'Modules' and num2 == 0:
                form.add_error('input2', 'Error: Modulus by zero')
            else:
                if operator == 'Power':
                    result = num1 ** num2
                elif operator == 'Modules':
                    result = num1 % num2
                elif operator == 'Average':
                    result = (num1 + num2) / 2
                elif operator == 'Max':
                    result = max(num1, num2)

                if result is not None:
                    if result > 500:
                        result -= 100
                    elif result % 2 == 0:
                        result /= 2

        return render(request, 'calculator_reco/result.html', {'form': form, 'result': result})
    else:
        form = CalculatorForm()
        return render(request, 'calculator_reco/math_form.html', {'form': form})