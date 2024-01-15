from django.shortcuts import render


def calc(request):
    return render(request, 'calc.html')


def calculate(request):
    if request.method == "POST":
        num1 = request.POST['number1']
        num2 = request.POST['number2']
        if 'add' in request.POST:
            ans = int(num1) + int(num2)
        elif 'subtract' in request.POST:
            ans = int(num1) - int(num2)
        elif 'divide' in request.POST:
            ans = int(num1) // int(num2)
        elif 'multiply' in request.POST:
            ans = int(num1) * int(num2)
    return render(request, 'calc.html', {'ans': ans})
