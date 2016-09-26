
def is_multiple(n, m):
   return not n%m


def is_even(k):
    even = "08642"
    return str(k)[-1] in even

def minmax(l):
    max, min = l[0], l[1]
    for i in l:
        min = i if i<min else min
        max = i if i>max else max
    return min, max
        
def seqSum(n):
    s=0
    for i in range(1, n):
        s+=i**2
    return s
        
    
s = sum([i**2 for i in range(1, 3) if not i % 2]) 

""" j=len(s)+k"""

print range(50, 81,10)
print range(8, -9, -2)
print [2**i for i in range(0,9)]

def myChose(l):
    return l[randrange(0,len(l))]

from random import *
#print myChose([1, 2, 4, 8, 16, 32, 64, 128, 256])

def myRevese(l):
    i = 0 
    while i<len(l)//2:
        l[i], l[len(l)-1-i] = l[len(l)-1-i], l[i]

def oddPairsDect(l):
    odd = [x for x in l if x%2]
    if odd.len()>1:
        return True
    else:
        return False

    
def isDis(l):
    d = {}
#   d[x]+=1 for x in l
    r = [x for x,v in d.iteritems() if v>1]
    if r :
        return r
    else :
        return False

if is_even(10) :
    print "Ture"
else:
    print "False"

#a = [x*x-x for x in range(10)]


def myShuffle(l):
    d = {}
    a = []
    while len(d)<len(l):
        s = randint(0, len(l)-1)
        a.append(l[s]) if not s in d else a
        d[s]=1
    return a

#print myShuffle([1, 2, 4, 8, 16, 32, 64, 128, 256])
        

import sys
def revlines():
    lines = sys.stdin.readlines()
    for l in reversed(lines):
        print l.replace("\n", '')

def dotp(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    print c
#dotp([1, 2, 3], [4, 5, 6])



def raseIndexError():
    l = [0,1, 2, 3]
    i = 4
    if i > len(l)-1:
        raise IndexError('dfdfdfdffd')
    else:
        l[i] = sds

def cnt_vol(s):
    v = 'aeiou'
    i = 0
    for c in s:
        if c in v:
            i+=1
    print i        
#cnt_vol('strength')

def remove_p(s):
    p = '\'\".,'
    n = []
    for c in s:
        if not c in p:
            n.append(c)
    print ''.join(n)
#remove_p("Let s try, Mike.")

def three_for():
    a = input()
    b = input()
    c = input()
    if a+b==c and a==b-c and a*b==c:
        print True
    else:
        print False
    
def factor(n):
    b = []
    k = 1
    while k*k < n:
        if n%k == 0:
            yield k
            b.append(n//k)
        k += 1
    if k*k == n:
        yield k
    for i in reversed(b):
        yield i
#for i in factor(100):
#    print i
    
def norm(v, p=2):
   return sum([i**p for i in v])**(1.0/p)

"""project"""

def all_range(s, t=''):
    if len(s) == 1:
        print t+s
    for c in s:
        all_range(s.replace(c,''), t+c)
#all_range('catdog')

def div(n):
    c = 0
    while n>=2:
        n=n/2.0
        c+=1
    return c 

"""make_change"""
def num_comp(n, m=[100, 50, 20, 5, 1, 0.5, 0.1]):
    r = []
    for i in m:
        r.append(n//i)
        n %= i
    return r
def make_change(c, g):
    m = [100, 50, 20, 5, 1, 0.5, 0.1]
    r = num_comp(g-c)
    for i in range(len(m)):
        print str(r[i]) + ' x ' + str(m[i])
#make_change(124.7, 200)

"""calu"""
def calu():
    while 1:
        l = raw_input()
        if not l.strip() :
            exit()
        if 'cl' in l :
            continue
        print eval(l)
#calu()
def cor_error(c):
    if ord(c) < 95:
        low = range(65, 91)
        low.remove(ord(c))
        return chr(choice(low))
    if ord(c) > 95:
        up = range(97, 122)
        up.remove(ord(c))
        return chr(choice(up))
def ran_write():
    l = "I will never spam my friends again."
    p = [l for i in range(100)]
    s = len(l) * 100
    c = 0
    used = []
    while c < 8:
        n = randrange(s)
        row, col = divmod(n, len(l))
        if l[col] in [".", " "] or n in used:
            continue
        used.append(n)
        p[row] = p[row].replace(p[row][col],cor_error(p[row][col]))
        c += 1
    for i in range(100):
        print str(i+1) + p[i]
#ran_write()

from time import *
from datetime import *
def random_birthday():
   s = datetime(2001, 1, 1, 0, 0, 0) 
   e = datetime(2004, 12, 31, 11, 59, 59)
   st = int(mktime(s.timetuple()))
   et = int(mktime(e.timetuple()))
   return localtime(randrange(st, et+1))
    

from collections import defaultdict
def birth_paradox(n):
    c = 0
    for i in range(n):
        t = [random_birthday() for i in range(23)]
        d = defaultdict(defaultdict)
        for b in t:
            if b.tm_mon in d.keys() and b.tm_mday in d[b.tm_mon].keys():
                c += 1
                break
            d[b.tm_mon][b.tm_mday]=1
    print c*1.0/n 

#birth_paradox(100)

def cnt_words(w):
    w = w.strip().split(" ")
    d = {}
    for s in w:
        if not s in d.keys():
            d[s]  = 1
        else:
            d[s]+=1

    print d
cnt_words("sdf lkjklj kljlkj sdsd sds sdsd d ss ss ss ")























































































































































































