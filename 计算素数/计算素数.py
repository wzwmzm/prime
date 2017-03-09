# -*- coding:utf-8 -*-
#   1, ss()求素数
#   2，ctrl-c 中断程序
#   3，w()保存素数列表到a.txt，运行变量到b.txt
#   4, r()读取保存的变量到内存
#   5, ss()再次运行求素数程序
import math
import time


list_num=[2]                 #存放算出的质数
i=3                     #待测数，不断递增
n=1                     #质数的编号
tab=100000              #统计区间的大小
ii=1                    #第几个统计区间
tem=0                   #上一区间最后一个质数编号用于计算本区间质数的数量

nn=1000000           #计算到第nn个质数时程序停止

def ss():
    global    list_num            #存放算出的质数
    global    i                     #待测数，不断递增
    global    n                    #质数的编号
    global    tab              #统计区间的大小
    global    ii
    global    tem

    while 1:
        ##tem1=i/2+1        
        tem1=int(math.sqrt(i))+1
        tem2=True
        
        for num in list_num:
            if num>tem1:break
            if i % num == 0 :
                tem2=False        
                break
        if tem2==True:      #得到一个质数
                list_num.append(i)
                n+=1
#                print(n,"---",i)
                if n==nn:   #计算到第nn个质数时程序停止
                    break    

        if i==ii*tab:
                print(ii*tab,"----------",n - tem)
                ii+=1
                tem = n

        i+=1


def w():
    ###########写入质数列表
    Li=[1,2,3,4,5,6]
    pre=str(list_num)
    pre=pre.replace("[","")
    pre=pre.replace("]","")+"\n"
    #print (pre)
    f=open("a.txt","w")
    f.write(pre)
    f.close()
    
    ###############写入运行时参数
    Li=[i,n,tab,ii,tem]
    pre=str(Li)
    pre=pre.replace("[","")
    pre=pre.replace("]","")+"\n"+"待测数，质数的编号，统计区间的大小，第几个统计区间，上一区间最后一个质数编号用于计算本区间质数的数量"
    f=open("b.txt","w")
    f.write(pre)
    f.close()


def r():
    global    list_num            #存放算出的质数
    global    i                     #待测数，不断递增
    global    n                    #质数的编号
    global    tab              #统计区间的大小
    global    ii
    global    tem
    
    ###########读取质数列表
    f=open("a.txt","r")
    iii=f.readline() 
    iii=iii.replace("\n","")
    Li=iii.split(",")
    f.close()
    #print (Li)
    list_num=[]
    for i in Li:
        list_num.append(int(i))

    ###############读取运行时参数
    f=open("b.txt","r")
    iii=f.readline() 
    iii=iii.replace("\n","")
    Li=iii.split(",")
    f.close()
    #print (Li)
    i,n,tab,ii,tem = int(Li[0]),int(Li[1]),int(Li[2]),int(Li[3]),int(Li[4])



###############为了计时用###################################
def main():              
    global list_num                 #存放算出的质数
    global i                     #待测数，不断递增
    global n                     #质数的编号
#    tab=100000              #统计区间的大小
    global ii                    #第几个统计区间
    global tem                   #另时计数用

    del list_num[:]
    list_num=[2]
    i=3
    n=1
    ii=1
    tem=0
    
    t1=time.time()
    ss()
    t2=time.time()
    print"-----------------------------------------"
    print"计算出了%d个质数，费时%f秒"%(nn,t2-t1)
    print"-----------------------------------------"



print"   1, ss()求素数"
print"   2，ctrl-c 中断程序"
print"   3，w()保存素数列表到a.txt，运行变量到b.txt"
print"   4, r()读取保存的变量到内存"
print"   5, ss()再次运行求素数程序"
print"   6, main(), 计算出nn个质数所花费的时间"
print"*********程序中的变量说明*********************************************"
print"      n                  最大质数编号"
print"      list_num[100]      第101个质数"
print"      i                  已经计算到几了     "
print"      nn                 计算到nn个质数程序停止, 可以将nn设置得很大，让程序一直运行下去"

main()
        
        


    




