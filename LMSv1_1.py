# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 08:56:03 2021

@author: Nahin
"""
from tkinter import *
username = None
password = None
print('Library Management System v1.0')
while username != 'admin' and password != 'admin':
    print('\n---LMS Starting---')
    username = input('username: ')
    password = input('password: ')
lms = dict()
type(lms)
lms["title"] = [None]
lms['author'] = [None]
try:
    title = open('title.txt')
    name = open('name.txt')
    for b in title:
        b = b.split()
        lms['title'].append(b[0])
    for b in name:
        b = b.split()
        lms['author'].append(b[0])
except:
    title = open('title.txt','w')
    name = open('name.txt','w')
a = True;
while a != 3 :
    print('\n1. Add New Book\n2. View List\n3. Exit')
    a = int(input('>>> '))
    if a == 1:
        lms['title'].append(input('Write Book title: '))
        lms['author'].append(input('Write Book author name: '))
    elif a == 2:
        try:
            rows = []
            tbl_title = ['Serial No.','Title','Author Name']

            for i in range(len(lms['title'])):

                cols = []

                for j in range(3):

                    e = Entry(relief=GROOVE)

                    e.grid(row=i, column=j, sticky=NSEW)
                    if i == 0:
                        e.insert(j,'%s' % (tbl_title[j]))
                    elif j == 0:
                        e.insert(END, '%d' % (i))
                    elif j == 1:
                        e.insert(END, '%s' % (lms['title'][i]))
                    elif j == 2:
                        e.insert(END, '%s' % (lms['author'][i]))
                    else:
                        pass
                    cols.append(e)

                rows.append(cols)

            mainloop()
            x = int(input('do you want to pick a book?\n1.Yes\n2.No\n>>> '))
            if x == 1:
                b = int(input('inter serial number of that book: '))
                print('Picked book:', b,'\t-\t', lms['title'][b],'\t-\t', lms['author'][b])
                print('\nchoose an option from this list below:')
                print('1. edit\n2. delete\n3. Dont want any change')
                y = int(input('>>> '))
                if y == 1:
                    lms['title'][b] = input('Give new title: ')
                    lms['author'][b] = input('give author name: ')
                elif y == 2:
                    del lms['title'][b]
                    del lms['author'][b]
                    print('selected book is deleted\n')
                else:
                    pass
        except:
            pass
    elif a == 3:
        break
    else:
        print("\nyou put an invalid input")
title = open('title.txt','w')
name = open('name.txt','w')
for i in range(1,len(lms['title'])):
    title.write(lms['title'][i])
    title.write('\n')
    name.write(lms['author'][i])
    name.write('\n')
title.close()
name.close()
    #z = int(input("Do you want to exit?\n1. yes\n2. no\n"))
