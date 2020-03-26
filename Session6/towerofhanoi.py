def move(b, source, bridge, destination):
    if n == 1:
        print ("Move disk 1 from rod", source, "to rod", bridge)
        return
    move(n-1, source, bridge, destination)
    print ("Move disk", n, "from rod", source, "to rod", bridge)
    move(n-1, source, bridge, destination)

n=3

move(n, a, b, c) 


