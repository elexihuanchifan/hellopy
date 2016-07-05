from django.http import HttpResponse
import pymysql
from django.shortcuts import render


# Create your views here.

def first_page(request):
    return HttpResponse("<p>洗浴</p>")


def staff(request):
    conn = pymysql.connect(host='localhost', port=3306, user='vamei', password='vameiisgood', db='villa',
                           charset='UTF8')
    cur = conn.cursor()
    user_list = cur.execute("SELECT * FROM USER")
    # staff_str = map(str, user_list);
    data = cur.fetchall()
    names = ''
    for item in data:
        names += item[1]

    cur.close()
    conn.commit()
    conn.close()
    return HttpResponse("<p>" + ''.join(names) + "</p>")


def templay(request):
    context = {}
    context['label'] = 'Hello World!'
    return render(request, 'templay.html', context)
