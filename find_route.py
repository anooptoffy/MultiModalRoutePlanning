#This is a brute a attempt to check if algo works
#It will be polished asap


"""
R= dictionary of routes {key=bus_stop : value= set of routes which crosses this stop} 
mypath = [list of bus_stops] <= outcome of our shortest route path
 
"""
R={'a':{1,2,3,4},
'b':{2,3,4,5},
'c':{3,4,5,6},
'd':{6,7}}

def find_route(mypath):
    j=len(mypath)
    start = mypath[0]
    res=set(R[start])
    i=1
    while i<j:
        n_res=R[mypath[i]]&res
        if n_res:
            c=1
        else:
            stop=mypath[i-1]
            print start+"->"+stop+":",res
            print "change bus"
            start=stop
            n_res=R[start]
            i=i-1
        i+=1
        res = n_res
    stop=mypath[i-1]
    print start + "->" + stop + ":", res


mypath=['a','b','c','d']
find_route(mypath)


