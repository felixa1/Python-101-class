soups = ['peper soup','okra soup','cassava soup','petetoe leaf soup','eforiro soup','garden egg soup','egg soup','egusi soup']
print(soups)

#Accessing Elements in a list
print(soups[4])

felix@feltech:~$ python3.10
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 + 3.0
4.0
>>> 3.9 ** 0.5
1.9748417658131499
>>> 3.0 ** 2
9.0
>>> 
>>> universe_age =14_000_000_000
>>> universe_age = 14_000_000_000
>>> print(universe_age)
14000000000
>>>  x,y,z = 0,0,0
  File "<stdin>", line 1
    x,y,z = 0,0,0
IndentationError: unexpected indent
>>> x,y,z = 0,0,0
>>> print('xyz')
xyz
>>> 3000 / 20 * 54 - 62 + 400 + 2100 / 7
8738.0
>>> * 5
  File "<stdin>", line 1
SyntaxError: can't use starred expression here
>>> 8738.0 * 0.5
4369.0
>>> 8738.0 * 5
43690.0
>>> 3000 + 3200 + 3300 + 3400 + 6900
19800
>>> 19800 / 5
3960.0
>>> 3960.0 * 5
19800.0
>>> 19800 \ 5
  File "<stdin>", line 1
    19800 \ 5
           ^
SyntaxError: unexpected character after line continuation character
>>> 19800 - 500
19300
>>> 19800 / 500
39.6
>>> 3*3*56*700-30*6000*62/7
-1241485.7142857143
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> soups = ['peper soup','okra soup','cassava soup','petetoe leaf soup','eforiro soup','garden egg soup','egg soup','egusi soup']
>>> print(soups)
['peper soup', 'okra soup', 'cassava soup', 'petetoe leaf soup', 'eforiro soup', 'garden egg soup', 'egg soup', 'egusi soup']
>>> print(soups[6)
  File "<stdin>", line 1
    print(soups[6)
                 ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> print(soups[6])
egg soup
>>> print(soups[6].title())
Egg Soup
>>> print(soups[6].title)
<built-in method title of str object at 0x7fa3efd0b070>
>>> print(soups[6].title())
Egg Soup
>>> print(soups[6].upper)
<built-in method upper of str object at 0x7fa3efd0b070>
>>> print(soups[6].upper())
EGG SOUP
>>> print(soups[0].upper())
PEPER SOUP
>>> print(soups[0].title())
Peper Soup
>>> print(soups[0].lower())
peper soup
>>> message = f'my first soup was a {soups[0].title()}.'
>>> print(message)
my first soup was a Peper Soup.
>>> message = f"my first soup was a {soups[0].title()}."
>>> 
>>> print(message)
my first soup was a Peper Soup.
>>> message = f"my first soup was a {soups[0].upper()}."
>>> print(message)
my first soup was a PEPER SOUP.
>>> message = 'my first soup was a {soups[0].title()}.'
>>> print(message)
my first soup was a {soups[0].title()}.
>>> message = 'my fourth soup was a {soups[5].title()}.'
>>> print(message)
my fourth soup was a {soups[5].title()}.
>>> message = 'my fouth soup was a {soups[5].title()}.'
>>> print(message)
my fouth soup was a {soups[5].title()}.
>>> message = f'my fourth soup was a {soups[5].title()}.'
>>> print(message)
my fourth soup was a Garden Egg Soup.
>>> message = f'my fourth soup was a {soups[3].title()}.'
>>> print(message)
my fourth soup was a Petetoe Leaf Soup.
>>> message = f'my fourth soup was a {soups[3,6].title()}.'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
>>> message = f'my fourth soup was a {soups[3][6].title()}.'
>>> print(message)
my fourth soup was a E.
>>> message = f'my fourth soup was a {soups[6].title()}.'
>>> print(message)
my fourth soup was a Egg Soup.
>>> 


#CHANGING ,ADDING AND REMOVING ELEMENTS. 

>>> Segs_friends = ['jide', 'tayo','lara', 'tolani','florence','gerarld','kelvin','chris','tom','jephtar','lucus','thompson']
>>> print(Segs_friends[4])
florence
>>> print{Segs_friends[4]}
  File "<stdin>", line 1
    print{Segs_friends[4]}
    ^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print(Segs_friends[o])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'o' is not defined
>>> print(Segs_friends[0])
jide
>>> print(Segs_friends[1])
tayo
>>> print(Segs_friends[2])
lara
>>> print(Segs_friends[3])
tolani
>>> print(Segs_friends[4])
florence
>>> print(Segs_friends[5])
gerarld
>>> print(Segs_friends[6])
kelvin
>>> print(Segs_friends[7])
chris
>>> print(Segs_friends[8])
tom
>>> print(Segs_friends[9])
jephtar
>>> print(Segs_friends[10])
lucus
>>> print(Segs_friends[11])
thompson
>>> print(Segs_friends[11].title())
Thompson
>>> print(Segs_friends[10].title())
Lucus
>>> print(Segs_friends[9].upper())
JEPHTAR
>>> print(Segs_friends[8].upper())
TOM
>>> print(Segs_friends[7].upper())
CHRIS
>>> print(Segs_friends[6].upper())
KELVIN
>>> print(Segs_friends[5].upper())
GERARLD
>>> print(Segs_friends[4].upper())
FLORENCE
>>> print(Segs_friends[3].upper())
TOLANI
>>> print(Segs_friends[2].upper())
LARA
>>> print(Segs_friends[1].upper())
TAYO
>>> print(Segs_friends[0].upper())
JIDE
>>> 
>>> letter= Hello jide, the event will be taking place at the barmoraal hall, at clinton close, los angelis tomorrow morning print(letter)
  File "<stdin>", line 1
    letter= Hello jide, the event will be taking place at the barmoraal hall, at clinton close, los angelis tomorrow morning print(letter)
                  ^^^^
SyntaxError: invalid syntax
>>> letter= Hello f'{Sege_friends[0], the event will be taking place at the barmoraal hall, at clinton close, los angelis tomorrow morning see you there!
  File "<stdin>", line 1
    letter= Hello f'{Sege_friends[0], the event will be taking place at the barmoraal hall, at clinton close, los angelis tomorrow morning see you there!
                  ^
SyntaxError: unterminated string literal (detected at line 1)
>>> letter= Hello f'{Sege_friends[0]}, the event will be taking place at the barmoraal hall, at clinton close,los angelis tomorrow morning see you there!
  File "<stdin>", line 1
    letter= Hello f'{Sege_friends[0]}, the event will be taking place at the barmoraal hall, at clinton close,los angelis tomorrow morning see you there!
                  ^
SyntaxError: unterminated string literal (detected at line 1)
>>> letter= Hello f'{Sege_friends[0]}, the event will be taking place at the barmoraal hall, at clinton close,los angelis tomorrow morning see you there!'
  File "<stdin>", line 1
    letter= Hello f'{Sege_friends[0]}, the event will be taking place at the barmoraal hall, at clinton close,los angelis tomorrow morning see you there!'
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax
>>> letter= Hello f'{Sege_friends[0]}',the event will be taking place at the barmoraal hall, at clinton close,los angelis tomorrow morning see you there!
  File "<stdin>", line 1
    letter= Hello f'{Sege_friends[0]}',the event will be taking place at the barmoraal hall, at clinton close,los angelis tomorrow morning see you there!
                  ^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax
>>> 
>>> letter = Hello f'{Sege_friends[0]}',the event will be taking place at the barmoral hall, at clinton close, los angelis tomorrow morning see you there!
  File "<stdin>", line 1
    letter = Hello f'{Sege_friends[0]}',the event will be taking place at the barmoral hall, at clinton close, los angelis tomorrow morning see you there!
                   ^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax
>>> letter = Hello f'(Sege_friends[0])',the event will be taking place at the barmoral hall, at clinton close'
  File "<stdin>", line 1
    letter = Hello f'(Sege_friends[0])',the event will be taking place at the barmoral hall, at clinton close'
                                                                                                             ^
SyntaxError: unterminated string literal (detected at line 1)
>>> letter = the event will be taking place at the barmoral hall, at clinton close,f"(Segs_friends[0].title()), see you there"
  File "<stdin>", line 1
    letter = the event will be taking place at the barmoral hall, at clinton close,f"(Segs_friends[0].title()), see you there"
                 ^^^^^
SyntaxError: invalid syntax
>>> letter = f"the event will be taking place at the barmoral hall, at clinton close,{Segs_friends[0].title()}, see you there"
>>> print(letter)
the event will be taking place at the barmoral hall, at clinton close,Jide, see you there
>>> letter = f"the event will be taking place at the barmoral hall, at clinton close,{Segs_friends[0].title()} !see you there"
>>> print(letter)
the event will be taking place at the barmoral hall, at clinton close,Jide !see you there
>>> letter = f"the event will be taking place at the barmoral hall, at clinton close,{Segs_friends[0].title()}! see you there"
>>> print(letter)
the event will be taking place at the barmoral hall, at clinton close,Jide! see you there
>>> 
>>> letter = f"the event will be taking place at the barmoral hall, at clinton close,{Segs_friends[1].upper()}! see you there"
>>> print(letter)
the event will be taking place at the barmoral hall, at clinton close,TAYO! see you there
>>> letter = f"{Segs_friends[2].upper()}!  the event will be taking place at the barmoral hall, at clinton close, see you there"
>>> print(letter)
LARA!  the event will be taking place at the barmoral hall, at clinton close, see you there
>>> letter = f"{Segs_friends[3].upper()}! the event will be taking place at the barmoral hall, at clinton close, see you there"
>>> print(letter)
TOLANI! the event will be taking place at the barmoral hall, at clinton close, see you there
>>> letter = f"Hello {Segs_friends[4].upper()}! the event will be taking place at the barmoral hall, at clinton close, see you there"
>>> print(letter)
Hello FLORENCE! the event will be taking place at the barmoral hall, at clinton close, see you there
>>> letter = f"Hello {Segs_friends[5].upper()}! the event will be taking place at the barmoral hall, at clinton close, see you there"
>>> print(letter)
Hello GERARLD! the event will be taking place at the barmoral hall, at clinton close, see you there
>>> letter = f"Hello {Segs_friends[6].upper()}! the event will be taking place at the barmoral hall, at clinton close, see you there"
>>> print(letter)
Hello KELVIN! the event will be taking place at the barmoral hall, at clinton close, see you there
>>> letter = f"Hello {Segs_friends[7].upper()}! the event will be taking place at the barmoral hall, at clinton close, dont forget to come with my booklets while coming, see you there"
>>> print(letter)
Hello CHRIS! the event will be taking place at the barmoral hall, at clinton close, dont forget to come with my booklets while coming, see you there
>>> 
>>> letter = f"Hello {Segs_friends[8].upper()}! the event will be taking place at the barmoral hall, at clinton close, dont forget to come with my booklets while coming, see you there"
>>> print(letter)
Hello TOM! the event will be taking place at the barmoral hall, at clinton close, dont forget to come with my booklets while coming, see you there
>>> 
>>> letter = f"Hello {Segs_friends[9].upper()}! the event will be taking place at the barmoral hall, at biden moore avenue, you may come with you girlfriend if you want,i have made pass provision for her, see you there!"
>>> print(letter)
Hello JEPHTAR! the event will be taking place at the barmoral hall, at biden moore avenue, you may come with you girlfriend if you want,i have made pass provision for her, see you there!
>>> 
>>> letter = f"Hello {Segs_friends[9].upper()} and Jude!, i just bought a brand new chevolt jeep with 84 firry cylnder, you've got to come now and let's celebrates it, am waiting to see you!"
>>> print(letter)
Hello JEPHTAR and Jude!, i just bought a brand new chevolt jeep with 84 firry cylnder, you've got to come now and let's celebrates it, am waiting to see you!
>>> letter = f"Hello {Segs_friends[9].upper()} and JUDE!, i just bought a brand new chevolet jeep with 84 firry cylnder, you've got to come now and let's celebrates it, am waiting to see you!"
>>> print(letter)
Hello JEPHTAR and JUDE!, i just bought a brand new chevolet jeep with 84 firry cylnder, you've got to come now and let's celebrates it, am waiting to see you!
>>> 
>>> 
>>> letter = f"Hello {Segs_friends[10].upper()} and TOMIWA!, i will be coming to the base by spring this year, but i need you to come and pick me at the JFK international airport, as the time draws closer i will keep you posted!"
>>> print(letter)
Hello LUCUS and TOMIWA!, i will be coming to the base by spring this year, but i need you to come and pick me at the JFK international airport, as the time draws closer i will keep you posted!
>>> 
>>> 
>>> letter = f"Hello {Segs_friends[11].upper()} and JIDE!, i will be coming to the base by spring this year,but i need you to come and pick me at the JFK international airport,i awear that you exams are just by the corner, so  as the time draws closer i will keep you posted!"
>>> 
>>> print(letter)
Hello THOMPSON and JIDE!, i will be coming to the base by spring this year,but i need you to come and pick me at the JFK international airport,i awear that you exams are just by the corner, so  as the time draws closer i will keep you posted!
>>> 
>>> letter = f"Hello {Segs_friends[11].upper()} and JIDE!, i will be coming to the base by spring this year,but i need both of you to come and pick me at the JFK international airport,i am awear that your exams are just by the corner, so  as the time draws closer i will keep you posted!"
>>> 
>>> print(letter)
Hello THOMPSON and JIDE!, i will be coming to the base by spring this year,but i need both of you to come and pick me at the JFK international airport,i am awear that your exams are just by the corner, so  as the time draws closer i will keep you posted!
>>> 


# HOW TO REMOVE AND MAKE SENTENCES ON A LIST
# del and .pop command

>>> mylist =['chervolet', 'carmry', 'jarguar', 'mersedise benz', 'innoson', 'G-wagon', 'land cruser', 'prado', 'parjero', 'rollroys', 'dulos', 'isuzu', 'elementor', 'seanar']
>>> print(mylist)
['chervolet', 'carmry', 'jarguar', 'mersedise benz', 'innoson', 'G-wagon', 'land cruser', 'prado', 'parjero', 'rollroys', 'dulos', 'isuzu', 'elementor', 'seanar']
>>> 
>>> 
>>> mylist.insert(0,'kawazakii')
>>> mylist.insert(5,'dawuoo')
>>> print(mylist)
['kawazakii', 'chervolet', 'carmry', 'jarguar', 'mersedise benz', 'dawuoo', 'innoson', 'G-wagon', 'land cruser', 'prado', 'parjero', 'rollroys', 'dulos', 'isuzu', 'elementor', 'seanar']
>>> mylist.insert('kangaro')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: insert expected 2 arguments, got 1
>>> 
>>> del mylist[0]
>>> del mylist[7]
>>> 
>>> print(mylist)
['chervolet', 'carmry', 'jarguar', 'mersedise benz', 'dawuoo', 'innoson', 'G-wagon', 'prado', 'parjero', 'rollroys', 'dulos', 'isuzu', 'elementor', 'seanar']
>>> 
>>> del mylist[7]
>>> print(mylist)
['chervolet', 'carmry', 'jarguar', 'mersedise benz', 'dawuoo', 'innoson', 'G-wagon', 'parjero', 'rollroys', 'dulos', 'isuzu', 'elementor', 'seanar']
>>> 
>>> mylist.insert(7,'prado'.title())
>>> mylist.insert(3,'prado'.upper())
>>> 
>>> print(mylist)
['chervolet', 'carmry', 'jarguar', 'PRADO', 'mersedise benz', 'dawuoo', 'innoson', 'G-wagon', 'Prado', 'parjero', 'rollroys', 'dulos', 'isuzu', 'elementor', 'seanar']
>>> 
>>> 
>>> mylist.insert(3,'picato'.upper(), 0,'isuzu tiger'.upper())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: insert expected 2 arguments, got 4
>>> 
>>> mylist.insert(3,'picato'.upper(),0 'isuzu tiger'.upper())
  File "<stdin>", line 1
    mylist.insert(3,'picato'.upper(),0 'isuzu tiger'.upper())
                                     ^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> 
>>> mylist.insert(3,'picato'.upper())
>>> mylist.insert(0 'isuzu tiger'.upper())
  File "<stdin>", line 1
    mylist.insert(0 'isuzu tiger'.upper())
                  ^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> mylist.insert(0,'isuzu tiger'.upper())
>>> 
>>> 
>>> print(mylist)
['ISUZU TIGER', 'chervolet', 'carmry', 'jarguar', 'PICATO', 'PRADO', 'mersedise benz', 'dawuoo', 'innoson', 'G-wagon', 'Prado', 'parjero', 'rollroys', 'dulos', 'isuzu', 'elementor', 'seanar']
>>> 
>>> 
>>> soups = ['peper soup','okra soup','cassava soup','petetoe leaf soup','eforiro soup','garden egg soup','egg soup','egusi soup']
>>> print(soups)
['peper soup', 'okra soup', 'cassava soup', 'petetoe leaf soup', 'eforiro soup', 'garden egg soup', 'egg soup', 'egusi soup']
>>> 
>>> 
>>> popped_soup = soups.pop()
>>> print(soups)
['peper soup', 'okra soup', 'cassava soup', 'petetoe leaf soup', 'eforiro soup', 'garden egg soup', 'egg soup']
>>> 
>>> print(popped_soup)
egusi soup
>>> 
>>> popped_soup = soups.pop
>>> print(popped_soup)
<built-in method pop of list object at 0x7f071c485a40>
>>> print(pop.soups)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pop' is not defined. Did you mean: 'pow'?
>>> 
>>> 
>>> print(popped_soup)
<built-in method pop of list object at 0x7f071c485a40>
>>> popped_soup = soups.pop(0)
>>> print(popped_soup)
peper soup
>>> 
>>> print(soups.pop)
<built-in method pop of list object at 0x7f071c485a40>
>>> print(soups)
['okra soup', 'cassava soup', 'petetoe leaf soup', 'eforiro soup', 'garden egg soup', 'egg soup']
>>> 
>>> first=soups.pop(0)
>>> 
>>> print(f'my first cooked soups in the house was a {first.upper().')
  File "<stdin>", line 1
    print(f'my first cooked soups in the house was a {first.upper().')
                                                                     ^
SyntaxError: f-string: expecting '}'
>>> print(f'my first cooked soups in the house was a {first.upper()}.')
my first cooked soups in the house was a OKRA SOUP.
>>> 
>>> print(f'my first cooked soups in the house was a {popped_soup.upper()}.')
my first cooked soups in the house was a PEPER SOUP.
>>> 
>>> print(f'my first cooked soups in the house was a {popped_soup.title()}.')
my first cooked soups in the house was a Peper Soup.
>>> 
>>> 

>>> 
>>> del mylist[0]
>>> del mylist[7]
>>> 
>>> print(mylist)
['chervolet', 'carmry', 'jarguar', 'mersedise benz', 'dawuoo', 'innoson', 'G-wagon', 'prado', 'parjero', 'rollroys', 'dulos', 'isuzu', 'elementor', 'seanar']
>>> 
>>> del mylist[7]
>>> print(mylist)
['chervolet', 'carmry', 'jarguar', 'mersedise benz', 'dawuoo', 'innoson', 'G-wagon', 'parjero', 'rollroys', 'dulos', 'isuzu', 'elementor', 'seanar']
>>> 
>>> mylist.insert(7,'prado'.title())
>>> mylist.insert(3,'prado'.upper())
>>> 
>>> print(mylist)
['chervolet', 'carmry', 'jarguar', 'PRADO', 'mersedise benz', 'dawuoo', 'innoson', 'G-wagon', 'Prado', 'parjero', 'rollroys', 'dulos', 'isuzu', 'elementor', 'seanar']
>>> 
>>> 
>>> mylist.insert(3,'picato'.upper(), 0,'isuzu tiger'.upper())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: insert expected 2 arguments, got 4
>>> 
>>> mylist.insert(3,'picato'.upper(),0 'isuzu tiger'.upper())
  File "<stdin>", line 1
    mylist.insert(3,'picato'.upper(),0 'isuzu tiger'.upper())
                                     ^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> 
>>> mylist.insert(3,'picato'.upper())
>>> mylist.insert(0 'isuzu tiger'.upper())
  File "<stdin>", line 1
    mylist.insert(0 'isuzu tiger'.upper())
                  ^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> mylist.insert(0,'isuzu tiger'.upper())
>>> 
>>> 
>>> print(mylist)
['ISUZU TIGER', 'chervolet', 'carmry', 'jarguar', 'PICATO', 'PRADO', 'mersedise benz', 'dawuoo', 'innoson', 'G-wagon', 'Prado', 'parjero', 'rollroys', 'dulos', 'isuzu', 'elementor', 'seanar']
>>> 
>>> 
>>> soups = ['peper soup','okra soup','cassava soup','petetoe leaf soup','eforiro soup','garden egg soup','egg soup','egusi soup']
>>> print(soups)
['peper soup', 'okra soup', 'cassava soup', 'petetoe leaf soup', 'eforiro soup', 'garden egg soup', 'egg soup', 'egusi soup']
>>> 
>>> 
>>> popped_soup = soups.pop()
>>> print(soups)
['peper soup', 'okra soup', 'cassava soup', 'petetoe leaf soup', 'eforiro soup', 'garden egg soup', 'egg soup']
>>> 
>>> print(popped_soup)
egusi soup
>>> 
>>> popped_soup = soups.pop
>>> print(popped_soup)
<built-in method pop of list object at 0x7f071c485a40>
>>> print(pop.soups)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pop' is not defined. Did you mean: 'pow'?
>>> 
>>> 
>>> print(popped_soup)
<built-in method pop of list object at 0x7f071c485a40>
>>> popped_soup = soups.pop(0)
>>> print(popped_soup)
peper soup
>>> 
>>> print(soups.pop)
<built-in method pop of list object at 0x7f071c485a40>
>>> print(soups)
['okra soup', 'cassava soup', 'petetoe leaf soup', 'eforiro soup', 'garden egg soup', 'egg soup']
>>> 
>>> first=soups.pop(0)
>>> 
>>> print(f'my first cooked soups in the house was a {first.upper().')
  File "<stdin>", line 1
    print(f'my first cooked soups in the house was a {first.upper().')
                                                                     ^
SyntaxError: f-string: expecting '}'
>>> print(f'my first cooked soups in the house was a {first.upper()}.')
my first cooked soups in the house was a OKRA SOUP.
>>> 
>>> print(f'my first cooked soups in the house was a {popped_soup.upper()}.')
my first cooked soups in the house was a PEPER SOUP.
>>> 
>>> print(f'my first cooked soups in the house was a {popped_soup.title()}.')
my first cooked soups in the house was a Peper Soup.
>>> 
>>> print(mylist
... print(mylist)
  File "<stdin>", line 1
    print(mylist
          ^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(list)
<class 'list'>
>>> 
>>> print( mylist )
['ISUZU TIGER', 'chervolet', 'carmry', 'jarguar', 'PICATO', 'PRADO', 'mersedise benz', 'dawuoo', 'innoson', 'G-wagon', 'Prado', 'parjero', 'rollroys', 'dulos', 'isuzu', 'elementor', 'seanar']
>>> 
>>> mylist.remove()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list.remove() takes exactly one argument (0 given)
>>> 
>>> mylist.remove ()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list.remove() takes exactly one argument (0 given)
>>> mylist.remove(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> 
>>> mylist.remove('seanar')
>>> 
>>> print(f'jude the seanar is constantly doing over heating and because of the double exhalte it consuming a lot of fuel now, for this reasons i have sold off today.
  File "<stdin>", line 1
    print(f'jude the seanar is constantly doing over heating and because of the double exhalte it consuming a lot of fuel now, for this reasons i have sold off today.
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> 
>>> print(f'jude the seanar is constantly doing over heating and because of the double exhalte it consuming a lot of fuel now, for this reasons i have sold off today.')
jude the seanar is constantly doing over heating and because of the double exhalte it consuming a lot of fuel now, for this reasons i have sold off today.
>>> 
>>> 
>>> popped_mylist = mylist.remove()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list.remove() takes exactly one argument (0 given)
>>> 
>>> removed_mylist = mylist.remove(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> 
>>> removed_mylist = mylist.remove(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> 
>>> removed_mylist = mylist.remove('carmry')
>>> print(f'jude the seanar is constantly doing over heating and because of the double exhalte it consuming a lot of fuel now, for this reasons i have sold off today.')
jude the seanar is constantly doing over heating and because of the double exhalte it consuming a lot of fuel now, for this reasons i have sold off today.
>>> 
>>> 
>>> (f'jude the seanar is constantly doing over heating and because of the double exhalte it consuming a lot of fuel now, for this reasons i have sold off today.')
'jude the seanar is constantly doing over heating and because of the double exhalte it consuming a lot of fuel now, for this reasons i have sold off today.'
>>> 
>>> print(f'Jude i think i am tired of the problems the {mylist.remove.upper()} is given me it unpresidented and i am completely fedup of it now, i want to sale it off.)
  File "<stdin>", line 1
    print(f'Jude i think i am tired of the problems the {mylist.remove.upper()} is given me it unpresidented and i am completely fedup of it now, i want to sale it off.)
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> 
>>> print(f'Jude i think i am tired of the problems the {mylist.remove.upper()} is given me it unpresidented and i am completely fedup of it now, i want to sale it off.')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'builtin_function_or_method' object has no attribute 'upper'
>>> 
>>> print(f'Jude i think i am tired of the problems the {'mylist.remove'.upper()} is given me it unpresidented and i am completely fedup of it now, i want to sale it off.')
  File "<stdin>", line 1
    print(f'Jude i think i am tired of the problems the {'mylist.remove'.upper()} is given me it unpresidented and i am completely fedup of it now, i want to sale it off.')
                                                          ^^^^^^
SyntaxError: f-string: expecting '}'
>>> 
>>> print(f'Jude i think i am tired of the problems the {mylist.remove .upper()} is given me it unpresidented and i am completely fedup of it now, i want to sale it off.')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'builtin_function_or_method' object has no attribute 'upper'
>>> 
>>> 
>>> print(f'Jude i think i am tired of the problems the {mylist.remove} is given me it unpresidented and i am completely fedup of it now, i want to sale it off.')
Jude i think i am tired of the problems the <built-in method remove of list object at 0x7f071c4a31c0> is given me it unpresidented and i am completely fedup of it now, i want to sale it off.
>>> 
>>> 
>>> print(f'Jude i think i am tired of the problems the {mylist.remove} is given me it unpresidented and i am completely fedup of it now, i want to sale it off.')
Jude i think i am tired of the problems the <built-in method remove of list object at 0x7f071c4a31c0> is given me it unpresidented and i am completely fedup of it now, i want to sale it off.
>>> 
>>> 
>>> print(f'Jude i think i am tired of the problems the {removed_mylist} is given me it unpresidented and i am completely fedup of it now, i want to sale it off.')
Jude i think i am tired of the problems the None is given me it unpresidented and i am completely fedup of it now, i want to sale it off.
>>> 
>>> 
>>> KISS = mylist.remove('carmry')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> 
>>> 
>>> mylist.remove('carmry')=KISS
  File "<stdin>", line 1
    mylist.remove('carmry')=KISS
    ^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
>>> 
>>> KISS='carmry'
>>> mylist.remove(KISS)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> 
>>> 
>>> KISS='carmry'
>>> print(f'\n The {KISS.title()} is problematic when it getting old.')

 The Carmry is problematic when it getting old.
>>> 
>>> print(mylist)
['ISUZU TIGER', 'chervolet', 'jarguar', 'PICATO', 'PRADO', 'mersedise benz', 'dawuoo', 'innoson', 'G-wagon', 'Prado', 'parjero', 'rollroys', 'dulos', 'isuzu', 'elementor']
>>> 
>>> pussycat = G-wagon
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'G' is not defined
>>> 
>>> pussycat ='G-wagon'
>>> mylist.remove(pussycat)
>>> print(f'friends for the love of hight and roughedity of volkwagon, i will go for  {pussycat.title()}.')
friends for the love of hight and roughedity of volkwagon, i will go for  G-Wagon.
>>> 
>>> mylist.remove('innoson')
>>> print(' considering the topography of the environment i will rather purchase{innoson.upper()} product')
 considering the topography of the environment i will rather purchase{innoson.upper()} product
>>> 
>>> 
>>> mylist.remove('innoson')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> 
>>> love ='innoson'
>>> print(' considering the topography of the environment i will rather purchase{love.upper()} product.')
 considering the topography of the environment i will rather purchase{love.upper()} product.
>>> 
>>> 
>>> print(f'considering the topography of the environment i will rather purchase{love.upper()} product.')
considering the topography of the environment i will rather purchaseINNOSON product.
>>> 
>>> print('considering the topography of the environment i will rather purchase {love.upper()} product.')
considering the topography of the environment i will rather purchase {love.upper()} product.
>>> 
>>> print(f'considering the topography of the environment i will rather purchase {love.upper()} product.')
considering the topography of the environment i will rather purchase INNOSON product.





Segs_friends = ['jide', 'tayo','lara', 'tolani','florence','gerarld','kelvin','chris','tom','jephtar','lucus','thompson']
>>> print(Segs_friends[4])
florence
>>> 
>>> invite= f'Dear{Segs_friends[0].upper()},this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.'  
>>> 
>>> print(invite)
DearJIDE,this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.
>>> 
>>> invite= f'Dear {Segs_friends[0].upper()},this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.'  
>>> 
>>> print(invite)
Dear JIDE,this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.
>>> 
>>> 
>>> invite= f'Dear {Segs_friends[5].upper()},this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.'  
>>> 
>>> print(invite)
Dear GERARLD,this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.
>>> 
>>> 
>>> invite= f'Dear {Segs_friends[10].upper()},this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.'  
>>> 
>>> 
>>> print(invite)
Dear LUCUS,this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.
>>> 
>>> 
>>> print(Segs_friends)
['jide', 'tayo', 'lara', 'tolani', 'florence', 'gerarld', 'kelvin', 'chris', 'tom', 'jephtar', 'lucus', 'thompson']
>>> 
>>> lov-2 ='lucus'
  File "<stdin>", line 1
    lov-2 ='lucus'
    ^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> lov-2 = ['lucus']
  File "<stdin>", line 1
    lov-2 = ['lucus']
    ^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> lov-2 = {'lucus'}
  File "<stdin>", line 1
    lov-2 = {'lucus'}
    ^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> 
>>> lov-2 = ('lucus')
  File "<stdin>", line 1
    lov-2 = ('lucus')
    ^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> lov-2 = 'lucus'
  File "<stdin>", line 1
    lov-2 = 'lucus'
    ^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> 
>>> lov-2 = f'lucus'
  File "<stdin>", line 1
    lov-2 = f'lucus'
    ^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> love = f'lucus'
>>> Segs_friends.remove{love}
  File "<stdin>", line 1
    Segs_friends.remove{love}
                       ^
SyntaxError: invalid syntax
>>> 
>>> Segs_friends.remove(love)
>>> print(Segs_friends)
['jide', 'tayo', 'lara', 'tolani', 'florence', 'gerarld', 'kelvin', 'chris', 'tom', 'jephtar', 'thompson']
>>> 
>>> king='jide'
>>> Segs_friends.remove(king)
>>> print(Segs_friends)
['tayo', 'lara', 'tolani', 'florence', 'gerarld', 'kelvin', 'chris', 'tom', 'jephtar', 'thompson']
>>> 
>>> Segs_friends.insert('Tope')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: insert expected 2 arguments, got 1
>>> 
>>> Segs_friends.insert(Tope)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Tope' is not defined. Did you mean: 'type'?
>>> 
>>> Segs_friends.insert 'Tope'
  File "<stdin>", line 1
    Segs_friends.insert 'Tope'
                        ^^^^^^
SyntaxError: invalid syntax
>>> Segs_friends.insert'Tope'
  File "<stdin>", line 1
    Segs_friends.insert'Tope'
                       ^^^^^^
SyntaxError: invalid syntax
>>> 
>>> Segs_friends.append('Tope')
>>> print(Segs_friends)
['tayo', 'lara', 'tolani', 'florence', 'gerarld', 'kelvin', 'chris', 'tom', 'jephtar', 'thompson', 'Tope']
>>> 
>>> Segs_friends.append('Otito')
>>> 
>>> Jungle='Otito'
>>> print(Segs_friends)
['tayo', 'lara', 'tolani', 'florence', 'gerarld', 'kelvin', 'chris', 'tom', 'jephtar', 'thompson', 'Tope', 'Otito']
>>> 
>>> pingy='Dear {Segs_friends'Jungle'.lower()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
  File "<stdin>", line 1
    pingy='Dear {Segs_friends'Jungle'.lower()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
                              ^^^^^^
SyntaxError: invalid syntax
>>> 
>>> pingy='Dear {Segs_friends[11].lower()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> pingy='Dear {Segs_friends[10].lower()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> 
>>> print(pingy)
Dear {Segs_friends[10].lower()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> pingy=f'Dear {Segs_friends[11].lower()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> 
>>> print(pingy)
Dear otito, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> pingy=f'Dear {Segs_friends[10].lower()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> 
>>> print(pingy)
Dear tope, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> pingy=f'Dear {Segs_friends'Jungle'.lower()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
  File "<stdin>", line 1
    pingy=f'Dear {Segs_friends'Jungle'.lower()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
                               ^^^^^^
SyntaxError: f-string: expecting '}'
>>> 
>>> pingy=f'Dear {'Jungle'.lower()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
  File "<stdin>", line 1
    pingy=f'Dear {'Jungle'.lower()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
                   ^^^^^^
SyntaxError: f-string: expecting '}'
>>> 
>>> print(Jungle)
Otito
>>> 
>>> print(king)
jide
>>> pingy=f'Dear {Segs_friends[10].upper()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> print(pingy)
Dear TOPE, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> pingy=f'Dear {Segs_friends[11].upper()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> 
>>> print(pingy)
Dear OTITO, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> pingy=f'Dear {Segs_friends[11].title()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> 
>>> print(pingy)
Dear Otito, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> pingy=f'Dear {Segs_friends[10].title()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> 
>>> print(pingy)
Dear Tope, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> 3-6. more guests
  File "<stdin>", line 1
    3-6. more guests
         ^^^^
SyntaxError: invalid syntax
>>> 
>>> print(Segs_friends)
['tayo', 'lara', 'tolani', 'florence', 'gerarld', 'kelvin', 'chris', 'tom', 'jephtar', 'thompson', 'Tope', 'Otito']
>>> Segs_friends[4].insert'kola'
  File "<stdin>", line 1
    Segs_friends[4].insert'kola'
                          ^^^^^^
SyntaxError: invalid syntax
>>> 
>>> 
>>> Segs_friends.insert(4,'kola')
>>> Segs_friends.insert(4,'shokoya')
>>> Segs_friends.insert(9,'shokoya')
>>> print(Segs_friends)
['tayo', 'lara', 'tolani', 'florence', 'shokoya', 'kola', 'gerarld', 'kelvin', 'chris', 'shokoya', 'tom', 'jephtar', 'thompson', 'Tope', 'Otito']
>>> 
>>> Segs_friends.append'omonla'
  File "<stdin>", line 1
    Segs_friends.append'omonla'
                       ^^^^^^^^
SyntaxError: invalid syntax
>>> Segs_friends.append(omonla)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'omonla' is not defined
>>> Segs_friends.append('omonla')
>>> Segs_friends.append('imoni')
>>> Segs_friends.insert(0,'imoni')
>>> Segs_friends.insert(6,'sharon sonko')
>>> 
>>> print(Segs_friends)
['imoni', 'tayo', 'lara', 'tolani', 'florence', 'shokoya', 'sharon sonko', 'kola', 'gerarld', 'kelvin', 'chris', 'shokoya', 'tom', 'jephtar', 'thompson', 'Tope', 'Otito', 'omonla', 'imoni']
>>> 
>>> 
>>> pingy=f'Dear {Segs_friends[0].title()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> 
>>> print(pingy)
Dear Imoni, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> pingy=f'Dear {Segs_friends[1].title()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> 
>>> print(pingy)
Dear Tayo, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> pingy=f'Dear {Segs_friends[2].title()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> 
>>> print(pingy)
Dear Lara, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> pingy=f'Dear {Segs_friends[3].title()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> 
>>> print(pingy)
Dear Tolani, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> pingy=f'Dear {Segs_friends[4].title()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> 
>>> print(pingy)
Dear Florence, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> 
>>> pingy=f'Dear {Segs_friends[5].title()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> 
>>> print(pingy)
Dear Shokoya, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> pingy=f'Dear {Segs_friends[6].title()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> 
>>> print(pingy)
Dear Sharon Sonko, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> pingy=f'Dear {Segs_friends[7].title()}, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.'
>>> 
>>> print(pingy)
Dear Kola, you are highly invited to the prestigious STAR GAZE musicall concert in memorial celebration of our founding fathers in faith.
>>> 
>>> 
>>> invite= f'Dear {Segs_friends[8].upper()},this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.'  
>>> 
>>> print(invite)
Dear GERARLD,this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.
>>> 
>>> invite= f'Dear {Segs_friends[9].upper()},this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.'  
>>> 
>>> print(invite)
Dear KELVIN,this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.
>>> 
>>> 
>>> invite= f'Dear {Segs_friends[10].upper()},this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.'  
>>> 
>>> print(invite)
Dear CHRIS,this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.
>>> 
>>> invite= f'Dear {Segs_friends[11].upper()},this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.'  
>>> 
>>> 
>>> print(invite)
Dear SHOKOYA,this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.
>>> 
>>> 
>>> invite= f'Dear {Segs_friends[12].upper()},this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.'  
>>> 
>>> 
>>> print(invite)
Dear TOM,this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.
>>> 
>>> 
>>> invite= f'Dear {Segs_friends[13].upper()},this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.'  
>>> 
>>> 
>>> print(invite)
Dear JEPHTAR,this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.
>>> 
>>> 
>>> invite= f'Dear {Segs_friends[14].upper()},this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.'  
>>> 
>>> print(invite)
Dear THOMPSON,this is an invitation to our gallar night at the barmoral hall, that will commence at 10am 12th of february 2023, you fine in your email a link to the VIP tags for you and your spouse, thanks see you there.
>>> 
>>> 
>>> del.Segs_friends
  File "<stdin>", line 1
    del.Segs_friends
       ^
SyntaxError: invalid syntax
>>> 
>>> del.Segs_friends[14]
  File "<stdin>", line 1
    del.Segs_friends[14]
       ^
SyntaxError: invalid syntax
>>> 
>>> del Segs_friends[14]
>>> del Segs_friends[13]
>>> 
>>> print(Segs_friends))
  File "<stdin>", line 1
    print(Segs_friends))
                       ^
SyntaxError: unmatched ')'
>>> print(Segs_friends)
['imoni', 'tayo', 'lara', 'tolani', 'florence', 'shokoya', 'sharon sonko', 'kola', 'gerarld', 'kelvin', 'chris', 'shokoya', 'tom', 'Tope', 'Otito', 'omonla', 'imoni']
>>> 

#this are essential variables syntex
del xxxx[the number of the position of WORD you want to delete].
xxxx.insert( 0 dis is the position, the thing you want bring in )
xxxx.append"Danjuma" dis will only add the numb from the top
xxxx.remove('mutiu') dis does not use numb's 

#Sortting your list alphabeltically, and reverse
friends.sort()
friends.sort(reverse=True) 









>>> 
>>> ['jude','comola','sumbo','lanre','femi']
['jude', 'comola', 'sumbo', 'lanre', 'femi']
>>> epep =['jude','comola','sumbo','lanre','femi']
>>> print(epep)
['jude', 'comola', 'sumbo', 'lanre', 'femi']
>>> epep[2].remove
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'remove'
>>> 
>>> epep.remove[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> 
>>> print(epep)
['jude', 'comola', 'sumbo', 'lanre', 'femi']
>>> 
>>> epep.pop
<built-in method pop of list object at 0x7f90f1bbc5c0>
>>> print(epep)
['jude', 'comola', 'sumbo', 'lanre', 'femi']
>>> 
>>> epep.append('kolade')
>>> print(epep)
['jude', 'comola', 'sumbo', 'lanre', 'femi', 'kolade']
>>> 
>>> epep.insert(3,'olade')
>>> print(epep)
['jude', 'comola', 'sumbo', 'olade', 'lanre', 'femi', 'kolade']
>>> 
>>> epep.insert(3,'jimoh')
>>> epep.insert(3,'mutiu')
>>> epep.insert(3,'aina')
>>> 
>>> print(epep)
['jude', 'comola', 'sumbo', 'aina', 'mutiu', 'jimoh', 'olade', 'lanre', 'femi', 'kolade']
>>> 
>>> epep.remve{3}
  File "<stdin>", line 1
    epep.remve{3}
              ^
SyntaxError: invalid syntax
>>> 
>>> epep.remve[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'remve'. Did you mean: 'remove'?
>>> epep.remve{3}
  File "<stdin>", line 1
    epep.remve{3}
              ^
SyntaxError: invalid syntax
>>> epep.remove[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> epep.remove(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> 
>>> epep.remove('3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> epep.remove'3'
  File "<stdin>", line 1
    epep.remove'3'
               ^^^
SyntaxError: invalid syntax
>>> epep.pop
<built-in method pop of list object at 0x7f90f1bbc5c0>
>>> 
>>> epep.pop'3'
  File "<stdin>", line 1
    epep.pop'3'
            ^^^
SyntaxError: invalid syntax
>>> pop.epep[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pop' is not defined. Did you mean: 'pow'?
>>> 
>>> pop.epep{2}
  File "<stdin>", line 1
    pop.epep{2}
            ^
SyntaxError: invalid syntax
>>> pop.epep'2'
  File "<stdin>", line 1
    pop.epep'2'
            ^^^
SyntaxError: invalid syntax
>>> 
>>> del epep'2'
  File "<stdin>", line 1
    del epep'2'
            ^^^
SyntaxError: invalid syntax
>>> del epep[2]
>>> print(epep)
['jude', 'comola', 'aina', 'mutiu', 'jimoh', 'olade', 'lanre', 'femi', 'kolade']
>>> del epep[2]
>>> print(epep)
['jude', 'comola', 'mutiu', 'jimoh', 'olade', 'lanre', 'femi', 'kolade']
>>> 
>>> epep.insert'aina'
  File "<stdin>", line 1
    epep.insert'aina'
               ^^^^^^
SyntaxError: invalid syntax
>>> epep.insert'aina'
  File "<stdin>", line 1
    epep.insert'aina'
               ^^^^^^
SyntaxError: invalid syntax
>>> 
>>> 
>>> epep.insert('aina')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: insert expected 2 arguments, got 1
>>> epep.insert(3,'aina')
>>> epep.insert(3,'sumbo')
>>> 
>>> print(epep)
['jude', 'comola', 'mutiu', 'sumbo', 'aina', 'jimoh', 'olade', 'lanre', 'femi', 'kolade']
>>> 
>>> epep.pop
<built-in method pop of list object at 0x7f90f1bbc5c0>
>>> epep[5].pop
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'pop'
>>> epep.pop'5'
  File "<stdin>", line 1
    epep.pop'5'
            ^^^
SyntaxError: invalid syntax
>>> epep.pop'mutiu'
  File "<stdin>", line 1
    epep.pop'mutiu'
            ^^^^^^^
SyntaxError: invalid syntax
>>> epep.pop('mutiu')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> epep.pop.3
  File "<stdin>", line 1
    epep.pop.3
            ^^
SyntaxError: invalid syntax
>>> epep.remove(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> epep.remove('mutiu')
>>> print(epep)
['jude', 'comola', 'sumbo', 'aina', 'jimoh', 'olade', 'lanre', 'femi', 'kolade']
>>> 
>>> pop(epep[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pop' is not defined. Did you mean: 'pow'?
>>> 
>>> 
>>> 
>>> ['tayo', 'lara', 'tolani', 'florence', 'gerarld', 'kelvin', 'chris', 'tom', 'jephtar', 'thompson', 'Tope', 'Otito']
['tayo', 'lara', 'tolani', 'florence', 'gerarld', 'kelvin', 'chris', 'tom', 'jephtar', 'thompson', 'Tope', 'Otito']
>>> friends=['tayo', 'lara', 'tolani', 'florence', 'gerarld', 'kelvin', 'chris', 'tom', 'jephtar', 'thompson', 'Tope', 'Otito']
>>> print(friends)
['tayo', 'lara', 'tolani', 'florence', 'gerarld', 'kelvin', 'chris', 'tom', 'jephtar', 'thompson', 'Tope', 'Otito']
>>> friends. sort()
>>> print(friends)
['Otito', 'Tope', 'chris', 'florence', 'gerarld', 'jephtar', 'kelvin', 'lara', 'tayo', 'thompson', 'tolani', 'tom']
>>> friends=['tayo', 'lara', 'tolani', 'florence', 'gerarld', 'kelvin', 'chris', 'tom', 'jephtar', 'thompson', 'tope', 'otito']
>>> 
>>> print(friends)
['tayo', 'lara', 'tolani', 'florence', 'gerarld', 'kelvin', 'chris', 'tom', 'jephtar', 'thompson', 'tope', 'otito']
>>> friends. sort()
>>> 
>>> print(friends)
['chris', 'florence', 'gerarld', 'jephtar', 'kelvin', 'lara', 'otito', 'tayo', 'thompson', 'tolani', 'tom', 'tope']
>>> 
>>> friends. sort(reverse=True)
>>> print(friends)
['tope', 'tom', 'tolani', 'thompson', 'tayo', 'otito', 'lara', 'kelvin', 'jephtar', 'gerarld', 'florence', 'chris']
>>> 
>>> friends. sort(reverse=true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> 
>>> print('friends:')
friends:
>>> print(friends)
['tope', 'tom', 'tolani', 'thompson', 'tayo', 'otito', 'lara', 'kelvin', 'jephtar', 'gerarld', 'florence', 'chris']
>>> 
>>> print('Here is the original list:')
Here is the original list:
>>> print('\nHere is the original list:')

Here is the original list:
>>> 
>>> print("\nHere is the original list:")

Here is the original list:
>>> friends. sort()
>>> print(friends)
['chris', 'florence', 'gerarld', 'jephtar', 'kelvin', 'lara', 'otito', 'tayo', 'thompson', 'tolani', 'tom', 'tope']
>>> 
>>> friends. sort(reverse.True)
  File "<stdin>", line 1
    friends. sort(reverse.True)
                          ^^^^
SyntaxError: invalid syntax
>>> 
>>> friends. sort()function
  File "<stdin>", line 1
    friends. sort()function
                   ^^^^^^^^
SyntaxError: invalid syntax
>>> 
>>> print(sorted(friends))
['chris', 'florence', 'gerarld', 'jephtar', 'kelvin', 'lara', 'otito', 'tayo', 'thompson', 'tolani', 'tom', 'tope']
>>> print(friends)
['chris', 'florence', 'gerarld', 'jephtar', 'kelvin', 'lara', 'otito', 'tayo', 'thompson', 'tolani', 'tom', 'tope']
>>> print(reverse=True(friends))
<stdin>:1: SyntaxWarning: 'bool' object is not callable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bool' object is not callable
>>> 
>>> 
>>> friends.reverse()
>>> print(friends)
['tope', 'tom', 'tolani', 'thompson', 'tayo', 'otito', 'lara', 'kelvin', 'jephtar', 'gerarld', 'florence', 'chris']
>>> 
>>> len(friends)
12
>>> 
felix@feltech:~$ python3.10
Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> donatuses = (654,092,8920,1243,3265)
  File "<stdin>", line 1
    donatuses = (654,092,8920,1243,3265)
                     ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> 
>>> donatuses = (654,92,8920,1243,3265)
>>> print(donatuses[0][3][1])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>> print(donatuses[0,3,1])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: tuple indices must be integers or slices, not tuple
>>> 
>>> print(donatuses[0])
654
>>> print(donatuses[3])
1243
>>> print(donatuses[2])
8920
>>> print(donatuses[1])
92
>>> print(donatuses[4])
3265
>>> print('originaldonatuses:')
originaldonatuses:
>>> print('original donatuses:')
original donatuses:
>>> print('Original donatuses:')
Original donatuses:
>>> for donatuse in donatuses:
...     print(donatuse)
... 
654
92
8920
1243
3265
>>> 
>>> donatuses = (654,92,7920,1250,3265)
>>> print('\nModified donatuses:')

Modified donatuses:
>>> for donatuse in donatuses:
...     print(donatuse)
... 
654
92
7920
1250
3265
>>> 
>>> buffet-menu=('cocnut bread','loiloi','fish pepersoup','edikaikon')
  File "<stdin>", line 1
    buffet-menu=('cocnut bread','loiloi','fish pepersoup','edikaikon')
    ^^^^^^^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> 
>>> buffetmenu = ('cocnut bread','loiloi','fish pepersoup','edikaikon')
>>> buffetmenus = ('cocnut bread','loiloi','fish pepersoup','edikaikon')
>>> 
>>> for buffetmenu in buffetmenus:
...     print(buffetmenu)
... 
cocnut bread
loiloi
fish pepersoup
edikaikon
>>> 
>>> buffetmenus = ('cocnut bread','loiloi','fish pepersoup','edikaikon','okra soup','Isiewu','goat pepersoup')
>>> print('\nmodify buffetmenus:')

modify buffetmenus:
>>> for buffetmenu in buffetmenus:
...     print(buffetmenu)
... 
cocnut bread
loiloi
fish pepersoup
edikaikon
okra soup
Isiewu
goat pepersoup
>>> 
>>> print('\tmodify buffetmenus:')
	modify buffetmenus:
>>> for buffetmenu in buffetmenus:
...     print(buffetmenu in buffetmenus)
... 
True
True
True
True
True
True
True
>>> 
>>> buffetmenus = ('cocnut bread','chiken and chips.upper()','loiloi','fish pepersoup','edikaikon','okra soup','Isiewu','goat pepersoup')
>>> print('\tmodify buffetmenus:')
	modify buffetmenus:
>>> for buffetmenu in buffetmenus:
...     print(buffetmenu in buffetmenus)
... 
True
True
True
True
True
True
True
True
>>> 
>>> buffetmenus = ('cocnut bread','chiken and chips.upper()','loiloi','fish pepersoup','edikaikon''Egusi soup','owu soup','goat pepersoup')
>>> print('\tmodify buffetmenus:')
	modify buffetmenus:
>>> for buffetmenu in buffetmenus:
...     print(buffetmenu)
... 
cocnut bread
chiken and chips.upper()
loiloi
fish pepersoup
edikaikonEgusi soup
owu soup
goat pepersoup
>>> 
>>> buffetmenus = ('cocnut bread','chiken and chips','loiloi','fish pepersoup','edikaikon','Egusi soup','owu soup','goat pepersoup')
>>> 
>>> print('\t modify buffetmenus:')
	 modify buffetmenus:
>>> for buffetmenu in buffetmenus:
...     print(buffetmenu.upper())
... 
COCNUT BREAD
CHIKEN AND CHIPS
LOILOI
FISH PEPERSOUP
EDIKAIKON
EGUSI SOUP
OWU SOUP
GOAT PEPERSOUP
>>> 
>>> print(buffetmenus[3])
fish pepersoup
>>> print(buffetmenus.upper[5])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'upper'
>>> 
>>> print(buffetmenus[5])
Egusi soup
>>> 
>>> print(buffetmenus.title())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'title'
>>> 
>>> print(buffetmenus)
('cocnut bread', 'chiken and chips', 'loiloi', 'fish pepersoup', 'edikaikon', 'Egusi soup', 'owu soup', 'goat pepersoup')
>>> for buffetmenu in buffetmenus:
...     print(buffetmenu.title())
... 
Cocnut Bread
Chiken And Chips
Loiloi
Fish Pepersoup
Edikaikon
Egusi Soup
Owu Soup
Goat Pepersoup
>>> 
