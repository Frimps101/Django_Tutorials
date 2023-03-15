from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Learn Data Structures",
    "february": "Learn Django",
    "march": "Apply for Jobs",
    "april": "Learn Algorithms",
    "may": "Learn Data Structures",
    "june": "Learn Django",
    "july": "Apply for Jobs",
    "august": "Learn Algorithms",
    "september": "Learn Data Structures",
    "october": "Learn Django",
    "november": "Apply for Jobs",
    "december": "Learn Algorithms",
}

# Create your views here.
# def index(request):
#     return HttpResponse("This works")

# def february(request):
#     return HttpResponse("Welcome to february")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if (month > len(months)):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenge/
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Invalid Month")
