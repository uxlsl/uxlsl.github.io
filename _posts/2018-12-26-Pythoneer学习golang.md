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


字符串定义

```

"hello, world"

```

*单引号*不是包围的不是字符串,只是一个int32


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

```

for {
}

```
select  与 chan 与 default

```

```

break goto 的降低版

## 中级

### 作用域

可以重新定义一个变量名相同的变量




### 错误处理
golang 倾向使用一个独立、明确的返回值来传递错误信息。
也就是类似c语言!

errors.New

```

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

```


## 通道

在python中相当于队列，可以使用包(比如queue,threading safe)实现
golang 这个内置到语言上实现

定义通道(考虑是否使用缓存)

messages = make(chan string)

放
messages <- "buffered"
取
msg <- messages


通道有趣的事
+ 使用通道做定时器
+ 使用通道做打点器
+ 使用通道进行同步
+ close chan for range chan

attend 
+ atomic in go
+ Mutex 

检查通道是否成功获取数据

```

if elem, ok := <-dataChan; ok {

```
单向通道主要用作函数参数,规约
<-chan
chan<-

### select 与通道,通道与超时

## defer 
defer 相当于python with 的使用,不过with with ,golang 实现要使用func func defer等

## 变量作用域
每个括号都有作用域
:=  初始化运算符


## 公共私有
golang 通过名字的首字母大小写决定，大写为公有，小写为私有


## 重要技巧

+ 查变量的类型 reflect.TypeOf(a)) ~ python type


## 常用包

+ strings 字符串处理 如大小写转换,重点包含Split,可以分割字符串



## 常用代码片


字符串分割
```

	s := "a\nb\nc\n"
	for i,v:= range strings.Split(s, "\n"){
		fmt.Println(i,v)
	}

```


## 相关名称

+ 并发字典, 可参考https://github.com/gopcp/example.v2的相关内容.


## 工具使用

### goland 编译并运行注意的问题
运行不成功，定义缺失,一般来说是运行类型与GOPATH设置不当所致,可以这样判断, 
go run main.go 定缺失,尝试go build ,然后再run,如果成功，就要在goland进行相应该设置run kind Directory

