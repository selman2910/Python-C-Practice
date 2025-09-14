def match(x,y):
    for i in y:
        if x==i:
            return i
    return "'"
def casematch(x,y):
    for i in y:
        if (i.lower())==(x.lower()):
            return i
    return "'"
def vovelmatch(x,y):
    list1 = ["A","a","E","e","I","i","U","u","O","o"]
    for a in y:
        b=a.upper()
        z=x.upper()
        if len(b)==len(z):
            control=1
            for i in range(len(b)):
                if z[i] in list1 and b[i] in list1:
                    continue
                elif (z[i] in list1 and b[i] not in list1) or (z[i] not in list1 and b[i] in list1):
                    control=0
                    break
                else:
                    if z[i]!=b[i]:
                        control=0
                        break
            if control:
                return a
    return "'"
def main():
    wordlist=["KiTe","kite","hare","Hare"]
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    output=[]
    for i in queries:
        list1=["'","'","'"]
        list1[0]=match(i,wordlist)
        if list1[0]!="'":
            output.append(list1[0])
            continue
        list1[1]=casematch(i,wordlist)
        if list1[1]!="'":
            output.append(list1[1])
            continue
        list1[2]=vovelmatch(i,wordlist)
        if list1[2]!="'":
            output.append(list1[2])
            continue
        output.append("'")
    for i2 in output:
        print(i2,end=" ")    
    
main()
            
        
            
        
