// primenum
package main

import (
	"fmt"
	"math"
	"runtime"
	"time"
)

const (
	maxproce int    = 8      //设置线程的数目
	maxnum   uint64 = 500000 //最大素数个数
	tab      uint64 = 100000 //统计区间的大小
	maxofgo  int    = 1000   //最大同时GO程数
)

var listNum [maxnum]uint64 //存放计算得出的素数

func main() {

	/////////////初始化--设置线程数////////////////////
	ps := runtime.GOMAXPROCS(maxproce)
	fmt.Printf("原始线程数 = %d,  现在设定线程数 = %d\n", ps, maxproce)

	if ps == 0 {
		fmt.Println("设置线程数失败!!！")
		return
	}
	//////////////初始化----////////////////////////////
	listNum[0] = 2
	i := uint64(3)   //待测数，不断递增
	n := uint64(0)   //质数的编号
	ii := uint64(1)  //第几个统计区间
	tem := uint64(0) //上一敬意最后一个质数编号，用于计算本区间质数个数
	//c := make(chan int)

	////求取质数
	s := func() {
		for {

			//////////////////func(i)(i,bool)  判断i是否为质数。用到的外部变量：   读listNum[]
			v, tem2 := func(uint64) (uint64, bool) { //i,v 相同，为被测试数， tem2 即为真假
				tem1 := uint64(math.Sqrt(float64(i))) + 1 //缩小范围
				tem2 := true                              //是否质数标志
				for num := uint64(0); num <= n; {         //计算i是不是质数
					if listNum[num] > tem1 { //超出范围了不是质数
						break
					}
					if i%listNum[num] == 0 {
						tem2 = false
						break
					}
					num++
				}
				return i, tem2
			}(i) //func(uint64) (uint64, bool)

			//////将所得质数存入listNum[]///////////////////////////////
			if tem2 == true { //得到一个质数，处理  外部变量：   n
				n++
				//println(n, "      ", v)

				listNum[n] = v     //将质数存入数组
				if n == maxnum-1 { //计算到第maxnum个质数时程序停止
					return
				}
			}

			if i == ii*tab { //打印“100000---------------6395”  外部变量： i,  ii,  tem,  n
				fmt.Printf("%d ------------------------------------ %d\n", ii*tab, n-tem)
				ii++
				tem = n
			}

			i++
			//println(i)
		} //for
	} //s

	t1 := time.Now()
	s()
	t2 := time.Since(t1)
	fmt.Printf("\n计算出了%v个质数，共花费时间 %v\n\n", maxnum, t2)
}
