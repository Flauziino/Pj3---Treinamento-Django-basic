from django.shortcuts import render


def home(request):
    context = {
            'text': 'Ola, home'
        }  # Uma view <<<< que recebe rquest e retorna sempre \
    return render(
        request,
        'home/index.html',
        context,
    )  # uma response!
