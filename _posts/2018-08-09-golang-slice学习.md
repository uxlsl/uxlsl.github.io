---
layout: post
title:
category: 学习
keywords: 学习,2016
---


# golang slice 学习

append 
如果切片底层数据没有足够的可用容量，append就会新建一个新的底层数组,
将被引用的现有值复制到新数组上，再追加新的值.


```

package main

import "fmt"

func main() {
	a := [2]int{1, 2}
	b := a[:]
	c := append(b, 10)
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	c[0] = 12

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
}

```
所以想使用切片共享数据,这点不可取
