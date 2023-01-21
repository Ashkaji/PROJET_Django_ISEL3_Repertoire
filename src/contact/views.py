from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from contact.models import Contact
from Repertoire.forms import ContactForm


def index(request):
    contacts = Contact.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form, 'contacts': contacts})


def update(request, pk):
    contact = Contact.objects.get(pk=pk)
    if "update" in request.POST:
        contact.name = request.POST.get('input-mod-name')
        contact.tel = request.POST.get('input-mod-tel')
        contact.save()
        return redirect("index")
    return render(request, 'update.html', {'contact': contact})


def delete(request, pk):
    contact = Contact.objects.get(pk=pk)
    if "delete" in request.POST:
        contact.delete()
        return redirect("index")
    elif "cancel" in request.POST:
        return redirect("index")
    return render(request, 'delete.html', {'contact': contact})
