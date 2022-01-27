import operator
def frequency(str):
    dict = {}
    for ch in str:
        if ch not in dict:
            dict[ch] = 1
        else:
            dict[ch]=dict[ch]+1
    dict2 = sorted(dict.items(),key= lambda kv:kv[1],reverse = True)
    
    print(dict2)


str = input("Input the string ")
frequency(str)
