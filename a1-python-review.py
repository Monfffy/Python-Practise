
# coding: utf-8

# ## Assignment 1 - Python Review
# ## Full name: Mengfei Hu
# ## andrew ID: mengfeih

# ### 1.i.
# ### The parse_hms function takes a string representation of a time duration,
# ### then returns a tuple of hours, minutes, and seconds.

def parse_hms(s):
    s = s.split(':')
    t = (int(s[0]),int(s[1]),int(s[2]))
    return (t)

parse_hms('0:45:00')

# ### 1.ii.
# ### The hms_to_seconds function takes three arguments: hours, minutes, and seconds,
# ### then returns the equivalent total number of seconds.

def hms_to_seconds(h,m,s):
    return (3600*h+60*m+s)

hms_to_seconds(0,33,37)


# ### 1.iii.
# ### The seconds_to_hms function takes a number of seconds,
# ### then returns a tuple of the equivalent in hours, minutes, and seconds.


def seconds_to_hms(s):
    h = int(s/3600)
    m = int((s-h*3600)/60)
    s = s-h*3600-m*60
    #print (h)
    #print (m)
    #print (s)
    hms = (h,m,s)
    return (hms)

seconds_to_hms(2017)

hms_to_seconds(*seconds_to_hms(54321))


# ### 1.iv.
# ### The sum_hms function takes an array of strings representing time durations and adds them.

def sum_hms(a):
    y = [hms_to_seconds(*(parse_hms(x))) for x in a]
    #print(sum(y))
    return (seconds_to_hms(sum(y)))

sum_hms(['3:00:00', '00:23:00', '0:0:45'])


# ### 2.
# ### The zeller function takes a year, month, and day,
# ### then returns a number from 0 to 6 representing the day of the week (0 - Sat.).

def zeller(y,m,d):
    if m <= 2:
        y = y-1
        m = m+12
    k = y%100
    j = y//100
    #print(k)
    #print(j)
    h = (d + (13*(m+1)//5) + k + (k//4) + (j//4) - (2*j))%7
    return h

zeller(2017,2,5)

# ### 3.a.
# ### The dice function randomly returns a integer from 1 to 6.

import random

def dice():
    return random.randint(1,6)

dice()

# ### 3.b.
# ### The six_in_4 function simulates the rolling of a dice 4 times and checks for the occurrence of a 6,
# ### then return Ture if a 6 occurs in the simulation and False otherwise.

def six_in_4():
    i = 1
    while i <= 4:
        x = dice()
        #print(x)
        i += 1
        if x == 6:
            return True
    return False

six_in_4()

# ### 3.c.
# ### The two_six_in_24 function simulates the rolling of two dice 24 times and checks for the occurrence of two 6s,
# ### then return Ture if a pair of 6s occur in the simulation and False if not.

def two_six_in_24():
    i = 1
    while i <= 24:
        x = dice()
        y = dice()
        #print(x)
        #print(y)
        i += 1
        if x == 6 and y == 6:
            return True
    return False

two_six_in_24()

# ### 3.
# ### The prob_question function perform both of six_in_4 and two_six_in_24 for n times,
# ### then return return the probability of occurrence of both events as a pair of numbers in a tuple,
# ### in the order of ( the probability of six_in_4, the probability of two_six_in_24 ).

def prob_question(n=10000):
    i = 1
    x = 0
    y = 0
    while i <= n:
        if six_in_4() == True:
            x += 1
        if two_six_in_24() == True:
            y += 1
        i += 1   
    #print(x)
    ##print(y)
    x = x/n
    y = y/n
    p = (x,y)
    #print(p)
    return (p)

prob_question(n=10000)

# ### 4.i.
# ### The calculate_avg_rating(data_file=’u.data’) function read from u.data file, 
# ### then returns a dictionary contains { movieid : average_rating , ... }.

def calculate_avg_rating(data_file='u.data'):
    f = open (data_file,'r')
    lines = f.readlines()
    #print(lines[0])
    dict_rating = {}
    #the following "for loop" create a dictionary where
    #key is the itemid (same as movieid) and 
    #the value is a list of all ratings for that itemid
    for line in lines:
        line = line.split()
        itemid = (line[1])
        #print(itemid)
        rating = []
        if itemid not in dict_rating:
            rating.append(int(line[2]))
            dict_rating[itemid] = rating
        else:
            old_rating = dict_rating.get(itemid)
            rating = old_rating[:]
            rating.append(int(line[2]))
            #print(rating)
            dict_rating[itemid] = rating
    #the following "for loop" modify the dictionary 
    #by replacing each value with the average of the array of ratings 
    for itemid in dict_rating.keys():
        avg_rating = sum(dict_rating[itemid])/len(dict_rating[itemid])
        dict_rating[itemid] = format(avg_rating, '.2f')
        #round(avg_rating,2)
    f.close()
    return dict_rating

calculate_avg_rating(data_file='u.data')


# ### 4.ii.reading function
# ### The read_u_item function read from u.item file, 
# ### then returns a dictionary contains { movieid : movie-title , ... }.

def read_u_item(data_file='u.item'):
    f = open (data_file,'r',encoding = 'latin-1')
    lines = f.readlines()
    dict_title = {}
    for line in lines:
        line = line.split('|')
        dict_title[line[0]] = line[1]
    f.close()
    return dict_title

read_u_item(data_file='u.item')


# ### 4.ii.
# ### The write_ratings function takes the avg_rating dictionary, 
# ### then writes output to fname in the following format:
# ### movieid rating movie-title
# ### also returns the sorted list of movie ratings.

def write_ratings(d,fname='movie-ratings.txt'):
    d_title = read_u_item(data_file='u.item')
    movie_rating = []
    for id in d.keys():
        if id in d_title.keys():
            movie_rating.append((id,d[id],d_title[id]))
    #print(movie_rating)
    sorted_movie = sorted(movie_rating,key=lambda x: x[1],reverse=True)
    #print(sorted_movie)
    f = open (fname,'w',encoding = 'utf-8')
    for i in range(len(sorted_movie)):
        f.write("%s\t" %(sorted_movie[i][0]))
        #print("%s\t" %(sorted_movie[i][0]))
        f.write("%s\t" %(sorted_movie[i][1]))
        #print("%s\t" %(sorted_movie[i][1]))
        f.write("%s\n" %(sorted_movie[i][2]))
        #print("%s\t" %(sorted_movie[i][2]))
    f.close()
    return (sorted_movie)

write_ratings(calculate_avg_rating(data_file='u.data'),fname='movie-ratings.txt')


# ### 5.
# ### Data source: http://finance.yahoo.com/quote/IBM/history?p=IBM (ibm.csv)
# ### Time period: Jan 1 2016 to Dec 31 2016
# ### It plot the Adj close values (y) against days (x) in range from 1 to len(y)

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

import csv

with open('ibm.csv', newline='') as csvfile:
       reader = csv.reader(csvfile)
       next(reader)
       y = []
       for row in reader:
           y.append(float(row[6]))
       y.reverse()
       #print(y)
       x = []
       for i in range(1,len(y)+1):
           x.append(i)
       #print(x)
       plt.plot(x,y)
       plt.xlabel('Days')
       plt.ylabel('Adj. Close Price')
       plt.title('Stock price of IBM in 2016')
csvfile.close()


