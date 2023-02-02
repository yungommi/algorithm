#10718
for i in range(0, 2):
    print("강한친구 대한육군")
    i += 1 

#10171
print('''\    /\\
 )  ( ')
(  /  )
 \(__)| ''')

#10172
print('''|\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\\__|''')



def function(input):
    a=input("input:")
    num=''
    for a in range (1, 1000):
        for b in range (a, 1000):
            for c in range (a, b+1):
                num += str(c)
            if a == input:
                return (str(a) + ' ' + str(b))

x=function(input)
print(x)





        

