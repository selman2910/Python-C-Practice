for i in range(1,101):
    if i%15==0:
        print(i,"fizzbuzz")
    elif i%3==0:
        print(i,"Fizz")
    elif i%5==0:
        print(i,"Buzz")
    else:
        continue
ogrenciler = {
    "Ali": [90, 85],
    "Ayşe": [100, 70]
}
while True:
    print("1 ekle\n2 list\n3 ort\n4 exit")
    x=int(input("your choice?"))
    match x:
        case 1:
            not1=[]
            a=input("name?")
            b=int(input("not1"))
            c=int(input("not2"))
            not1.extend([b,c])
            ogrenciler[a]=not1
        case 2:
            for a,b in ogrenciler.items():
                print(a,b)
        case 3:
            for a,b in ogrenciler.items():
                top=0
                for c in b:
                    top+=c
                ort=top/len(b)
                print(a,ort)
        case 4:
            print("bye bye")
            break
    
            
        
        