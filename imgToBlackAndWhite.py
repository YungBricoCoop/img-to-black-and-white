from PIL import Image as A 
b = A.open("c.jpg") 
d = [[x,y] for x in range(b.size[0]) for y in range(b.size[1])] 
e = [[sum(x) for x in [(0,0,0),(255,255,255)]].index(min(list([sum(x) for x in [(0,0,0),(255,255,255)]]), key=lambda x:abs(x-sum(b.getpixel((e[0],e[1])))))) for e in d] 
[ b.putpixel((d[x][0],d[x][1]),(0,0,0) if e[x] == 0 else (255,255,255)) for x in range(len(e))] 
b.save("f.jpg") 
b.show() 
