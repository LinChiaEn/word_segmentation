statement=input()
listA=[]
answer=[]
file=open("dict_no_space.txt",mode="r",encoding="utf-8")
for line in file:
    listA.append(line[0:len(line)-1])
file.close()
listA.reverse()

while(len(statement)!=0):
    append_success=0
    engNum=0
    if(statement[0:1]=='，' or statement[0:1]=='。' or statement[0:1]=='、'):
        append_success=1
        answer.append(statement[0:1])
        statement=statement[1:]
    elif(ord(statement[0])>64 and ord(statement[0])<91):
        engNum+=1
        while(ord(statement[engNum])>64 and ord(statement[engNum])<91):
            engNum+=1
        answer.append(statement[:engNum])
        statement=statement[engNum:]
    else:
        for element in listA:
            if(statement[0:len(element)]==element):
                append_success=1
                answer.append(element)
                statement=statement[len(element):]
                break
        
print(answer)

