from django.shortcuts import render
from django.core.files.base import ContentFile
import openai
import os
import requests
from dotenv import load_dotenv
from generator.models import Img


load_dotenv()

api_key = os.getenv("IMG_KEY", None)
openai.api_key = api_key


def generate_img(request):
    obj = None
    if api_key is not None and request.method == "POST":
        user_input = request.POST.get("user_input")
        response = openai.Image.create(prompt=user_input, size="512x512")

        img_url = response["data"][0]["url"]

        response = requests.get(img_url)
        img_file = ContentFile(response.content)

        count = Img.objects.count() + 1
        fname = f"image-{count}.jpg"

        obj = Img(name=user_input)
        obj.img.save(fname, img_file)
        obj.save()
    return render(request, "index.html", {"object": obj})
