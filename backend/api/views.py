from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .ocr.extractor import extract_text


def upload_image(request):

    extracted_text = ""

    if request.method == 'POST' and request.FILES.get('image'):

        image = request.FILES['image']

        fs = FileSystemStorage()

        filename = fs.save(image.name, image)

        image_path = fs.path(filename)

        extracted_text = extract_text(image_path)

    return render(request, 'upload.html', {
        'text': extracted_text
    })