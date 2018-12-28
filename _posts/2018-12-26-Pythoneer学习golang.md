---
layout: post
title: Pythonneer学习golang
category: 学习
keywords: 学习,2018
---


## 基本
小结：golang 原则能少定义类型就少定义类型(所以很多时候类型在后)，让编译器推导类型
变量定义:

```

var a = 100

```

数组定义(注意初始化使用了{):

```

var a = [10]int{1,2,3,4,5,6,7,8,9,10}

```

关联数组定义：

```

m = make(map[string]int)

```
结构定义:

```

type persion struct {
	name string
}

```
函数定义:

```

func add(x int, y int) int {
}

```

for 使用:

```

for ; ; {
}

```

```


for k,v := range m {
}


```

## 中级
### 错误处理
golang 倾向使用一个独立、明确的返回值来传递错误信息。
也就是类似c语言!
errors.New

import "errors"


func f1() (int, error) {
	return 1, errors.New("hello")
}
func main(){
	v, e := f1()
	if e != nil {
		fmt.Println(v)
	}
}
