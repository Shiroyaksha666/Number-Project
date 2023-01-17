yekan = ['' , 'yek' , 'do' , 'se' , 'chahar' , 'panj' , 'shesh' , 'haft' , 'hasht' , 'noh' , 'dah', 'yazdah' , 'davazdah' , 'sizdah' , 'chahardah' , 'panzdah' , 'shanzdah' , 'hefdah' , 'hijdah' , 'noozdah']
dahgan = ['' , 'dah' , 'bist' , 'si' , 'chehel' , 'panjah' , 'shast' , 'haftad' , 'hashtad' , 'navad']
sadgan = ['' , 'sad' , 'divist' , 'sisad' , 'chaharsad' , 'paansad' , 'sheshsad' , 'haftsad' , 'hashtsad' , 'nohsad']
namad = ['' , 'hezar' , 'milion' , 'miliyard' , 'trilion' , 'triliard' , 'kadriliard' , 'kointilion' , 'koantiniard' , 'sikstilion' , 'sikstiliard' , 'septilion' , 'septiliard' , 'octilion' , 'octiliard' , 'nanilion' , 'naniliard' , 'desilion' , 'desiiard' , 'andeselion' , 'andesiliard' , 'dodsilion']
Number = input('Enter your number: ')
Numberdigit = len(Number)
adad = []
Result = []
if Number == '0':
    print('sefr')
else:
    Numberdevider = list(divmod(Numberdigit, 3))
    for i in range(Numberdevider[0] + 1):
        adad.append(Number[Numberdigit - (i * 3) - 3 : Numberdigit - (i * 3)])
    try:
        adad.remove('')
    except ValueError:
        pass 
       
    adad.append(Number[0 : Numberdigit - ((Numberdevider[0] * 3))])    
    adad.reverse()
namad2 = len(adad) - 1
try:
    adad.remove('')
except ValueError:
        pass 
if int(Number) < 100:
    del adad[1]        
adad2 = [int(x) for x in adad]
z = len(adad)
for i in adad2:
    z -= 1
    if i == 0:
        pass
    elif 0 < i < 20:
        Result.append(f'{yekan[i]} {namad[z]}')  
    elif 19 < i < 100:
        a = i // 10
        b = i % 10
        if b == 0:
            Result.append(f'{dahgan[a]} {namad[z]}')
        else:
            Result.append(f'{dahgan[a]} o {yekan[b]} {namad[z]}')        
    elif 99 < i < 1000:
        c = i // 100
        d = (i % 100) // 10
        e = i % 10
        if e == 0 and d == 0:
            Result.append(f'{sadgan[c]} {namad[z]}')
        elif d == 0:
            Result.append(f'{sadgan[c]} o {yekan[e]} {namad[z]}') 
        elif e == 0:
            Result.append(f'{sadgan[c]} o {dahgan[d]} {namad[z]}')
        else:
            if i - (c * 100) > 20:
                Result.append(f'{sadgan[c]} o {dahgan[d]} o {yekan[e]} {namad[z]}')
            else:
                Result.append(f'{sadgan[c]} o {yekan[e]} {namad[z]}')
total = ''
for i in Result:
    total = total + 'o ' + i
print(total.split(maxsplit = 1)[1])
#Code by Ali Esmkhani