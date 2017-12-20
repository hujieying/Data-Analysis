# encoding=utf-8

import numpy as np

def main():
    lst=[[1,3,5],[2,4,6]]
    print(type(lst))
    np_list=np.array(lst)
    print(type(np_list))
    np_list=np.array(lst,dtype=np.float)
    print(np_list.shape)
    print(np_list.ndim)  #维数
    print(np_list.dtype)
    print(np_list.itemsize) #每个元素大小
    print(np_list.size)

if __name__=="__main__":
    main()
