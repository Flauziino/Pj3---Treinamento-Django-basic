from django.shortcuts import render
from blog.data import posts
from django.http import Http404


def blog(request):
    context = {
            # 'text': 'Ola, blog',
            'posts': posts
        }
    return render(
        request,
        'blog/index.html',
        context,
    )


def post(request, id):
    found_post = None
    for post in posts:
        if post['id'] == id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Pagina nao encontrada')

    context = {
            # 'text': 'Ola, blog',
            'post': found_post,
            'title': post['title'] + '-'
        }
    return render(
        request,
        'blog/post.html',
        context,
    )


def exemplo(request):
    context = {
            'text': 'Ola, exemplo',
            'title': 'Essa pg é um exemplo -'
        }
    return render(
        request,
        'blog/exemplo.html',
        context,
    )
