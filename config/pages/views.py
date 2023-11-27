from django.views.generic import TemplateView
import re
from tinydb import TinyDB
from django.shortcuts import redirect


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class MySelfPageView(TemplateView):
    template_name = "myself.html"


def requestURL(request):
    if request.method == 'GET':
        answer = request.GET.get('url', '')

        db = TinyDB('db.json')

        def validate_phone_number(phone_number):
            item = db.get(doc_id=1)
            pattern = rf'{item["phone"]}'
            return bool(re.match(pattern, phone_number))

        def validate_email(email):
            item = db.get(doc_id=1)
            pattern = rf'{item["email"]}'
            return bool(re.match(pattern, email))

        def validate_date(date):
            item = db.get(doc_id=1)
            pattern = rf'{item["date"]}'
            return bool(re.match(pattern, date))

        templates = answer.split('&')
        templates = [i.split('=') for i in templates]

        dictionary = {}

        for template in templates:
            if len(template) == 2:
                key, value = template
                dictionary[key] = value

        for key, value in dictionary.items():
            if validate_date(value) == True:
                db.insert({key: "data"})
            elif validate_phone_number(value) == True:
                db.insert({key: "phone"})
            elif validate_email(value) == True:
                db.insert({key: "email"})
            else:
                db.insert({key: "text"})

    return redirect("http://127.0.0.1:8000/")