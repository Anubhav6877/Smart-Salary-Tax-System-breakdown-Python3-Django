from django.shortcuts import render

def salary_view(request):
    context = {}

    if request.method == "POST":
        context = {
            "basic": float(request.POST.get("basic", 0)),
            "hra_percent": float(request.POST.get("hra_percent", 0)),
            "bonus": float(request.POST.get("bonus", 0)),
            "allowance": float(request.POST.get("allowance", 0)),
            "pf_percent": float(request.POST.get("pf_percent", 0)),
            "tax_percent": float(request.POST.get("tax_percent", 0)),
        }

    return render(request, "salaryy.html", context)

