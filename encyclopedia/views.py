from django.shortcuts import render

from . import util

import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"La entrada '{title}' no existe."
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": markdown2.markdown(content)
    })