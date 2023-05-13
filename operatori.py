def suma():
    print('Suma')
    print('Introduceti a')
    a = input()
    print("s a introdus primul nr. adica a=", a )
    print('Introduceti b')
    b = input()
    print("s a introdus al doilea nr. adica b=", b)
    print("adunarea a+b= ", int(a)+int(b))


def scaderea():
     print('Scaderea')
     print('Introduceti a')
     a = input()
     print("s a introdus primul nr. adica a=", a)
     print('Introduceti b')
     b = input()
     print("s a introdus al doilea nr. adica b=", b)
     print('scaderea a-b= ', int(a) - int(b))


def aria():
    print('Arie triunghi dreptunghic')
    print('Introduceti cateta 1')
    a = input()
    print("s a introdus prima cateta adica ab/c1", a)
    print('Introduceti cateta 2')
    b = input()
    print("s a introdus a 2-a cateta adica ac/c2", b)
    print('aria = c1c2/2 = ', int(a) int(b) / 2)


def perimetru():
    print('Perimetru triunghi')
    print('Introduceti latura 1')
    a = input()
    print("s a introdus prima latura adica ab", a)
    print('Introduceti latura 2')
    b = input()
    print("s a introdus a 2-a latura adica bc", b)
    print('Introduceti latura 3')
    c = input()
    print("s a introdus a 3-a latura adica ac", c)
    print('perimetru ab+bc+ac = ', int(a) + int(b) + int(c))

def ariaDreptunghi():
    print('Arie dreptunghi')
    print('Introduceti lungimea')
    a = input()
    print("s a introdus lungimea adica L", a)
    print('Introduceti latimea')
    b = input()
    print("s a introdus latimea adica l", b)
    print('aria Ll = ', int(a) int(b))

if name == 'main':
     suma()
     scaderea()
     aria()
     perimetru()
     ariaDreptunghi()