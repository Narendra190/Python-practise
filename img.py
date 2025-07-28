f1=open("img.jpg","rb")
image=f1.read()
print(image)

f2=open("img3.jpg","wb")
f2.write(image)
