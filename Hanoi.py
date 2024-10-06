def t(h,s,aux,e):
    if h>=1:
        print("line1")
        t(h-1,s,e,aux)
        print("line2")
        print("moving disk from",h,s,"to",e)
        print("line3")
        t(h-1,aux,s,e)

t(3,"A","B","C")        
