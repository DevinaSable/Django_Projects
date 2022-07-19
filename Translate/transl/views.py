from django.shortcuts import render, HttpResponse
from translate import Translator
from django.core.exceptions import ValidationError
# Create your views here.

def home(request):
    text = ''
    translation = ''
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]
        translator = Translator(to_lang=language)
        translation = translator.translate(text)
        return render(request, "transl/index.html", {"translation": translation, "text": text})
    return render(request,"transl/index.html")

    # return translation, text
#    return render(request, "transl/index.html", text, translation )
