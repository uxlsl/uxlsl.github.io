package main

import "fmt"

func main() {
	// 不写长度写法
	a := [...]int{1, 2, 3, 4}
	fmt.Println(a)
	// 不写哪种 历遍数组
	for i, v := range a {
		fmt.Println(i, v)
	}
	a1 := a[1:3]
	// 切片的实现，长度，容量
	fmt.Println(a1, len(a1), cap(a1))
}
