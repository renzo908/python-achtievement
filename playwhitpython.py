Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+2
4
>>> 3*10
30
>>> 100-10
90
>>> 25/5
5.0
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> print('mijn naam is
      
SyntaxError: EOL while scanning string literal
>>> print('mijn naam is renzo')
mijn naam is renzo
>>> print (renzo)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print (renzo)
NameError: name 'renzo' is not defined
>>> print (naam)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print (naam)
NameError: name 'naam' is not defined
>>> print( naam )
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print( naam )
NameError: name 'naam' is not defined
>>> NameError: name 'naam' is not defined
SyntaxError: invalid syntax
>>> naam = 'renzo'
>>> Print (renzo)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    Print (renzo)
NameError: name 'Print' is not defined
>>> print (naam)
renzo
>>> print (naam.upper())
RENZO
>>> print(naam[0:2])
re
>>> print(naam[::-1])
ozner
>>> leeftijd = 15
>>> hoelang_tot18jaar = 18 - leeftijd
>>> print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
Over 3 jaar wordt je 18
>>> leeftijd = 16
>>> 
KeyboardInterrupt
>>> 
>>> leeftijd = 16
>>> hoelang_tot18jaar = 18 - leeftijd
>>> print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
Over 2 jaar wordt je 18
>>> leeftijd > 19:
	
SyntaxError: invalid syntax
>>> leeftijd = 19
>>> hoelang_al18jaar = leeftijd - 18
>>> print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
Het is alweer 1 jaar geleden dat je 18 werd ;-)
>>> print('Je bent precies ' + str(leeftijd) + ' jaar')
Je bent precies 19 jaar
>>> from random import randint
randint(0,1000)
willekeurig_getal = randint(0,1000)
willekeurig_getal
print('willekeurig getal tussen de 0 en 1000: ' + str(willekeurig_getal))

from datetime import datetime
datum = datetime.now()
print(datum)
datum.strftime('%A %d %C %Y')

import locale
locale.setlocale(locale.LC_TIME, 'nl_NL')
datum.strftime('%A %d %B %Y')
locale.setlocale(locale.LC_TIME, 'it_IT')
datum.strftime('%A %d %B %Y')
