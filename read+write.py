
f1=open("write.txt","r+")
print(f1.tell())
print(f1.read())
print(f1.tell())
f1.write("hello everyone")
print(f1.tell())