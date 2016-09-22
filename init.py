# -*- coding: utf-8 -*-
import csv
import os
import time
import sys


def timer(f):
    """Таймер функции"""
    coding = sys.stdin.encoding
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print "Время выполнения функции: %f".decode('UTF-8').encode(coding) % (time.time()-t)
        return res
    return tmp


def get_filelist(month, day, year, service):
    coding = sys.stdin.encoding
    if __name__ == "__main__":
        if month == '':
            month = '05'
        if day == '':
            day = '05'
        if year == '':
            year = '2014'
        service = raw_input('Введите услугу(1 Альт, 2 Мастер, 3 Дез):'.decode('UTF-8').encode(coding))
    if len(day) == 1:
        day = '0' + day
    if len(month) == 1:
        month = '0' + month
    dpap = day + '_' + month + '_' + day
    if service == '1':
        directory = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap + '/' u'альт'
    elif service == '2':
        directory = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap + '/' u'мастер'
    elif service == '3':
        directory = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap + '/' u'дез'
    elif service == '0':
        directory = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap
    else:
        directory = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap
    files = os.listdir(directory)
    files = filter(lambda x: x.endswith('.txt'), files)
    files = [directory + '/' + fil for fil in files]
    return files



def search_csv(files, search_str):
    listf = []
    search_str = unicode(search_str, 'utf-8')
    for fil in files:
#        print fil
        reader = csv.reader(open(fil, "rb"))
        for row in reader:
            row = ", ".join(row)
            row = unicode(row, 'cp866')
            if search_str.upper() in row:
                 listf.append(row)
    return listf

def main():
    coding = sys.stdin.encoding
    day = raw_input('Введите нужный день:'.decode('UTF-8').encode(coding))
    month = raw_input('Введите нужный месяц:'.decode('UTF-8').encode(coding))
    year = raw_input('Введите нужный год:'.decode('UTF-8').encode(coding))
    search_str = raw_input('Введите искомую строку:'.decode('UTF-8').encode(coding))
    search_csv(get_filelist(month, day, year, ''), search_str)
    

if __name__ == "__main__":
    while True:
        main()
