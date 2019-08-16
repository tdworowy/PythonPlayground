import os

from django.shortcuts import render

from dlinks.forms import SkypeDataForm
from dlinks.get_links_ import SkypeApi, write_to_file_no_duplicates

PATH = os.path.dirname(os.path.abspath(__file__))


def post_skype_data(request):
    links = open(PATH + '\links.txt', 'r').readlines()
    aut = open(PATH + '\\aut.txt', 'r').readlines()
    if request.method == 'POST':
        skypeData_form = SkypeDataForm(data=request.POST)
        if skypeData_form.is_valid():
            skypeData = skypeData_form.save(commit=False)
            skypeData.save()
            sa = SkypeApi(aut[0].strip(), aut[1])
            links = sa.get_links(skypeData.chatName)
            write_to_file_no_duplicates(PATH + "\links.txt", links)
    else:
        skypeData_form = SkypeDataForm()

    return render(request, 'dlinks/form.html',
                  {'skypeData_form': skypeData_form, "links": links})
