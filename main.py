#try num 0

def placeRot(__array,__n):
    __tmp = []
    for idx,x in enumerate(__array):
        if(idx+1 == len(__array)):
            __tmp.append(__array[idx+1-len(__array)])
        else:
            __tmp.append(__array[idx+1])
    __array = __tmp
    print(__tmp)

#try num 1

def rotNtimes(__array,__n):
    if (__n == len(__array)):
        print(__array)
        return __array
    if (__n > len(__array)):
        for n in range(__n%len(__array)):
            __tmp = []
            for idx,x in enumerate(__array):
                if(idx+1 == len(__array)):
                    __tmp.append(__array[idx+1-len(__array)])
                else:
                    __tmp.append(__array[idx+1])
        __array = __tmp
        print(__array)
        return __array

    if (__n < len(__array)):
        for n in range(__n):
            __tmp = []
            for idx,x in enumerate(__array):
                if(idx+1 == len(__array)):
                    __tmp.append(__array[idx+1-len(__array)])
                else:
                    __tmp.append(__array[idx+1])
            __array=__tmp
        __array = __tmp
        print(__array)
        return __array
      
#try num 2 (final)

def rot2Left(arr,n):
    if (n == len(arr)):
        return arr
    if (n > len(arr)):
        return arr[n%len(arr):len(arr)] + arr[0:n%len(arr)]
    if (n < len(arr)):
        print(arr[n:len(arr)] + arr[0:n])
        return arr[n:len(arr)] + arr[0:n]
