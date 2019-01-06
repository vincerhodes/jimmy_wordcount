from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()

    word_dictionary = {}

    for word in word_list:
        word_caps = str(word).lower()
        if word_caps in word_dictionary:
            # Increase number
            word_dictionary[word_caps] += 1
        else:
            # Add to the dictionary
            word_dictionary[word_caps] = 1

    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext,
                                          'wordcount': len(word_list),
                                          'word_dictionary': word_dictionary,
                                          'word_list': word_dictionary.items(),
                                          'sorted_words': sorted_words})


def about(request):
    return render(request, 'about.html')
