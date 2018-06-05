Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ('Hello Word')
Hello Word
>>> print ("Hello")
Hello
>>> Print ("Hello")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    Print ("Hello")
NameError: name 'Print' is not defined
>>> print (hello)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print (hello)
NameError: name 'hello' is not defined
>>>  print (hello)
SyntaxError: unexpected indent
>>> 2+2
4
>>> 2-1
1
>>> 2*2
4
>>> 2**4
16
>>> 2**10
1024
>>> 2*10000
20000
>>> 2 ** 10000
19950631168807583848837421626835850838234968318861924548520089498529438830221946631919961684036194597899331129423209124271556491349413781117593785932096323957855730046793794526765246551266059895520550086918193311542508608460618104685509074866089624888090489894838009253941633257850621568309473902556912388065225096643874441046759871626985453222868538161694315775629640762836880760732228535091641476183956381458969463899410840960536267821064621427333394036525565649530603142680234969400335934316651459297773279665775606172582031407994198179607378245683762280037302885487251900834464581454650557929601414833921615734588139257095379769119277800826957735674444123062018757836325502728323789270710373802866393031428133241401624195671690574061419654342324638801248856147305207431992259611796250130992860241708340807605932320161268492288496255841312844061536738951487114256315111089745514203313820202931640957596464756010405845841566072044962867016515061920631004186422275908670900574606417856951911456055068251250406007519842261898059237118054444788072906395242548339221982707404473162376760846613033778706039803413197133493654622700563169937455508241780972810983291314403571877524768509857276937926433221599399876886660808368837838027643282775172273657572744784112294389733810861607423253291974813120197604178281965697475898164531258434135959862784130128185406283476649088690521047580882615823961985770122407044330583075869039319604603404973156583208672105913300903752823415539745394397715257455290510212310947321610753474825740775273986348298498340756937955646638621874569499279016572103701364433135817214311791398222983845847334440270964182851005072927748364550578634501100852987812389473928699540834346158807043959118985815145779177143619698728131459483783202081474982171858011389071228250905826817436220577475921417653715687725614904582904992461028630081535583308130101987675856234343538955409175623400844887526162643568648833519463720377293240094456246923254350400678027273837755376406726898636241037491410966718557050759098100246789880178271925953381282421954028302759408448955014676668389697996886241636313376393903373455801407636741877711055384225739499110186468219696581651485130494222369947714763069155468217682876200362777257723781365331611196811280792669481887201298643660768551639860534602297871557517947385246369446923087894265948217008051120322365496288169035739121368338393591756418733850510970271613915439590991598154654417336311656936031122249937969999226781732358023111862644575299135758175008199839236284615249881088960232244362173771618086357015468484058622329792853875623486556440536962622018963571028812361567512543338303270029097668650568557157505516727518899194129711337690149916181315171544007728650573189557450920330185304847113818315407324053319038462084036421763703911550639789000742853672196280903477974533320468368795868580237952218629120080742819551317948157624448298518461509704888027274721574688131594750409732115080498190455803416826949787141316063210686391511681774304792596709376
>>> 4/2
2.0
>>> 3/2
1.5
>>> 42
42
>>> 3.1415
3.1415
>>> type(52)
<class 'int'>
>>> type(3.1415)
<class 'float'>
>>> type('texto')
<class 'str'>
>>> id(42)
1479595712
>>> a = 42
>>> id(a)
1479595712
>>> id(42)
1479595712
>>> id('abacate')
61583072
>>> b='abacate'
>>> id(b)
61583072
>>> 2 * a
84
>>> c = a + 5
>>> id(c)
1479595792
>>> id(a + 5)
1479595792
>>> c
47
>>> 
======= RESTART: C:/Users/TR520596/Documents/Python Scripts/zombie.py =======
5
>>> 
======= RESTART: C:/Users/TR520596/Documents/Python Scripts/zombie.py =======
45
>>> 
======= RESTART: C:/Users/TR520596/Documents/Python Scripts/zombie.py =======
Abacate e Maçã
>>> dir('abacate')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help('abacate'.upper)
Help on built-in function upper:

upper(...) method of builtins.str instance
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> 
>>> a = 42
>>> b = 32
>>> a > b
True
>>> b > a
False
>>> type(True)
<class 'bool'>
>>> a == 42
True
>>> b == 32
True
>>> a != 13
True
>>> a
42
>>> nota 7
SyntaxError: invalid syntax
>>> nota = 7
>>> faltas = 30
>>> nota >= 7 and faltas <= 20
False
>>> a = 42
>>> b = 42
>>> a == 42 or b == 42
True
>>> b = 13
>>> a == 42 or b == 42
True
>>> a = 13
>>> a == 42 or b == 42
False
>>> print ('O numero é ' + a)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    print ('O numero é ' + a)
TypeError: must be str, not int
>>> print ('O numero é ', a)
O numero é  13
>>> print ('O numero é', a, 'muito legal')
O numero é 13 muito legal
>>> print ('O numero é %d muito legal', %a)
SyntaxError: invalid syntax
>>> print ('O numero é %d muito legal' %a)
O numero é 13 muito legal
>>> a = 'abacate'
>>> print ('A fruta %s é muito gostosa, na opnião dele')
A fruta %s é muito gostosa, na opnião dele
>>> print ('A fruta %s é muito gostosa, na opnião dele' %a)
A fruta abacate é muito gostosa, na opnião dele
>>> a = 3.1415
>>> print ('O valor de PI é %f' %a)
O valor de PI é 3.141500
>>> print ('O valor de PI é %2f' %a)
O valor de PI é 3.141500
>>> print ('O valor de PI é %.2f' %a)
O valor de PI é 3.14
>>> a = 42
>>> a
42
>>> a + 'mamão'
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a + 'mamão'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(42) + 'mamão'
'42mamão'
>>> a
42
>>> b
13
>>> a , b = b , a
>>> a
13
>>> b
42
>>> a, b, c = 1, 2, 3
>>> a
1
>>> b
2
>>> c
3
>>> a, b, c = 'OBA'
>>> a
'O'
>>> b
'B'
>>> c
'A'
>>> 

>>> 
