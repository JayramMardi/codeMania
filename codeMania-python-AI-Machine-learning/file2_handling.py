f=open("a.txt","w")
f.write(" Oops THIS FILE IS DELETED OR NO LONGER SUPOORTED   this is me and you /n,")

f.close()

# now this text has been added in the text file now print it.

f=open("a.txt","r")
print(f.readline())

