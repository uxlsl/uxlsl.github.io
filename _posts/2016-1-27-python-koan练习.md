---
layout: post
title: python-koan 传心练习
category: 学习
keywords: 学习,2016
---

##  Python Koans - Learn Python through TDD
![](http://7xnnj6.com1.z0.glb.clouddn.com/koan.jpg)

## 安装使用

```

git clone http://github.com/gregmalcolm/python_koans
cd python_koans

cd python2
python2 contemplate_koans.py
# or
cd python3
python3 contemplate_koans.py


```

## 方法
In test-driven development the mantra has always been, red, green,
refactor. Write a failing test and run it (red), make the test pass
(green), then refactor it (that is look at the code and see if you
can make it any better). In this case you will need to run the koan
and see it fail (red), make the test pass (green), then take a
moment and reflect upon the test to see what it is teaching you and improve the code to better communicate its intent

**重构测试然后想想学到了什么,并且尝试怎样修改从而接近原意!**


## emacs 技巧

1. M + %
2. C + W
editing
3. C + M + c
4. n

goto 2

## 关于字符串(about_string.py)

  test_adjacent_strings_are_concatenated_automatically
  test_double_quoted_strings_are_strings
  test_escaping_quotes_at_the_end_of_triple_quoted_string
  test_most_strings_interpret_escape_characters
  test_plus_concatenates_strings
  test_plus_equals_also_leaves_original_string_unmodified
  test_plus_equals_will_append_to_end_of_string
  test_plus_will_not_modify_original_strings
  test_raw_strings_are_also_strings
  test_single_quoted_strings_are_also_strings
  test_triple_quote_strings_are_also_strings
  test_triple_quoted_strings_can_span_lines
  test_triple_quoted_strings_need_less_escaping
  test_triple_single_quotes_work_too
  test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line
  test_use_backslash_for_escaping_quotes_in_strings
  test_use_double_quotes_to_create_strings_with_single_quotes
  test_use_single_quotes_to_create_string_with_double_quotes

### 总结

+ 字符串的表达方式
    1. "str"
    2. 'str'
    3. """"str""""

+ 字符串中使用 " '
  1. "包围使用'"
  2. '包围"'
  3. '\'' | "\""

+ 字符串换行
  1. "\n形式", '\n形式'
  2. """
  形式
  """"
  3. '''
  形式
  '''

+ 字符串比较
不同形式比较是相等的

#### 技巧
1. 如果字符串中有',尽量使用",
2. 如果字符串中有",尽量使用',
3. 如果多行使用"""|'''

```

In [8]: 'hello' == "hello" == """hello"""
Out[8]: True


```

## 关于None

1. test_none_is_an_object
2. test_none_is_universal
3. test_what_exception_do_you_get_when_call_nonexistent_methods
4. test_none_is_distinct

1. none 是一个对象
2. none 是唯一
3. 会异常
4. none 不是 0 ,不是False

assertRegexpMatches

总结:
第3点经常会出现,注意AttributeError,会提高解决问题效率.


## 关于列表(about_list)

  test_accessing_list_elements
  test_creating_lists
  test_insertions has
  test_list_literals
  test_lists_and_ranges
  test_making_queues
  test_popping_lists
  test_ranges_with_steps
  test_slicing_lists
  test_slicing_to_the_edge


*有趣的句子*
part of the python philosophy is that there ideally should be one
only one way of doing anything
这也许就是有pop 没有 push的原因吧!

### 总结:
1. 创造列表
2. 列表区间赋值
3. 列表的访问, 正,负访问
4. 列表的切片
5. 列表插入
6. append与pop
7. range, 起,止,步长,*注意负值情况*


``` 2

In [12]: a = range(10)

In [13]: a
Out[13]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [14]: a[2:3] = ['a','b','c']

In [15]: a
Out[15]: [0, 1, 'a', 'b', 'c', 3, 4, 5, 6, 7, 8, 9]


```

### range 负步长情况

range(5, 3, -1)


## 列表的赋值 (AboutListASSignments)

  test_non_parallel_assignment
  test_parallel_assignments
  test_parallel_assignments_with_extra_values
  test_parallel_assignments_with_sublists
  test_swapping_with_parallel_assignment

*总结*
列表一次性贼值给多个变量


```

first_name, last_name = last_name, first_name


```


## 关于字典(about_dictionaries)

test_creating_dictionaries
test_dictionary_literals
test_accessing_dictionaries
test_changing_dictionaries
test_dictionary_is_unordered
test_dictionary_keys_and_values
test_making_a_dictionary_from_a_sequence_of_keys


### 总结:

1. 字典的创造
2. 字典的访问
3. 字典的修改
4. 字典的无序性
5. 字典的key和values
6. 字典的fromkeys

技巧
使用fromkeys向多个健赋相同的值


```

In [29]: cards = {}.fromkeys(('red warrior', 'green elf', 'blue valkyrie',
                             'yellow dwarf', 'confused looking zebra'), 42)
In [30]:
In [30]: cards
Out[30]:
{'blue valkyrie': 42,
 'confused looking zebra': 42,
 'green elf': 42,
 'red warrior': 42,
 'yellow dwarf': 42}


```


## 字符串操作(AboutStringManipulation)

test_use_format_to_interpolate_variables
test_formatted_values_can_be_show_in_any_order_or_be_repeated
test_any_python_expression_my_by_interpolated
test_you_can_get_substring_from_a_string
test_you_can_get_a_single_character_from_a_string
test_single_characters_can_be_represented_be_integers
test_strings_can_be_split
test_strings_can_be_split_with_different_patterns
test_raw_strings_do_not_interpret_escape_characters
test_strings_can_be_joined
test_strings_can_change_case

### 总结
1. 字符串的格式化
2. 字符串的分割
3. 字符串的联合


```

In [9]: decimal_places = 4

In [10]: "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
   ....: decimal_places)
Out[10]: 'The square root of 5 is 2.2361'

In [11]: import datetime

In [12]: d = datetime.datetime(2010, 7, 4, 12, 15, 58)

In [13]: '{:%Y-%m-%d %H:%M:%S}'.format(d)


```

*If the implementation is easy to explain, it may be a good idea.*


## 元组(AboutTuples)
test_creating_a_tuple
test_tuples_are_imutable_so_item_assignment_is_not_possible
test_tuples_are_imutable_so_appending_is_not_possible
test_tuples_can_only_be_changed_through_replacement
test_tuples_of_one_look_peculiar
test_tuple_constructor_can_be_surprising
test_creating_empty_tuples
test_tuples_can_be_embedded
test_tuples_are_good_for_representing_records

### 总结

1. 元组的创建
2. 元组的*不可变性*
3. *一个元素的元组*, 容易出错
4. 空的元组
5. 元组的嵌套
6. 元组的更改


```

('one') == 'one'# True
('one', ) # 一个元素的元组写法
tuple() # 推荐空元组的写法

#一个元素的表达可能和下面有关

("hello"
 "world"
)

```


## 方法(aboutMethods)

+ test_calling_a_global_function
  如何看是全局函数?
  定义时,def左边已经没空格了
+ test_callings_functions_with_wrong_number_of_arguments
 会出现
    1. missing reqired positional arguments
    2. takes   positional arguments but

+ test_which_does_not_return_anything
没有返回值会出现什么情况?

+ test_calling_with_default_values
默认值的情况

+ test_calling_with_variable_arguments
args 会是什么类型呢?

+ test_functions_without_self_arg_are_global_functions
+ test_calling_methods_in_same_class_with_explicit_receiver


测试没有self.的函数是什么函数,这个最令我吃惊的是打印了hi



```
def hello():
    print ("hello")


class man(object):
    def hello(self):
        def hello():
            print ("hi")
        hello()

man().hello()


```

+ test_that_old_methods_are_hidden_by_redefinitions
+ test_that_overlapped_method_is_still_there

    def another_method_with_the_same_name(self):
        return 10

    link_to_overlapped_method = another_method_with_the_same_name

方法赋值法,使相同功能的函数在一起

+ test_methods_that_do_nothing_need_to_use_pass_as_a_filler
+ test_pass_does_nothing_at_all


测试发现还是会执行的

+ test_the_documentation_can_be_viewed_with_the_doc_method

方法的__doc__文档


+ test_calling_methods_in_other_objects
+ test_private_access_is_implied_but_not_enforced
+ test_attributes_with_double_underscore_prefiex_are_subject_to_name_mangling

测试私有方法的 _, __,
吃惊, 双下划线的还是可以访问的.


## 关于控制语句(AboutControlStatements)

+ test_if_then_else_statements
+ test_if_then_statements
+ test_if_then_elif_else_statements
+ test_while_statement
+ test_break_statement
+ test_continue_statement
+ test_for_statement
+ test_for_statement_with_tuples

总结:
主要讲了if ,elif,else,while,break,continue,for, for with tuple的使用!


**Now is better than never.**

## 关于控制语句的条件(about_true_and_false)

+ test_true_is_treated_as_true
+ test_false_is_treated_as_false
+ test_none_is_treated_as_false
+ test_zero_is_treated_as_false
+ test_empty_collections_are_treated_as_false
+ test_blank_strings_are_treated_as_false
+ test_everything_else_is_treated_as_true

总结:
条件的True,False,直接看作,True,False
其他的就有条件了
任何为空的都可以看作False,如None,[],{},(),空字符串,set()
其他的就看作True



**Namespaces are one honking great idea -- let's do more of those!**


## 关于集合(AboutSets)

test_sets_make_keep_lists_unique
通过列表初始化成集合会去重
test_empty_sets_have_different_syntax_to_populated_sets
集合的不同表示
test_dictionaries_and_sets_use_same_curly_braces
注意集合与字典都使用了括号
test_set_have_arithmetic_operators
集合的不同操作 &^|
test_we_canquery_set_membership
test_we_can_compare_subsets
集合的比较

### 总结

1. 集合初始化
2. 集合与字典的共同点
3. 集合的操作



## AboutTriangle

test_equiateral_triangles_have_equal_sides
test_isosceles_triangles_have_exactly_two_sides_equal
test_scalene_triangles_have_no_equal_sides

惊人地发现
a == b | b == c | a == c 表达式是不对的


*Flat is better than nested.*

## 关于异常(about_exceptions)

test_exceptions_inherit_from_exception
异常的继承
test_try_clause
test_raising_a_specific_error
test_else_clause
test_finally_clause


### 总结
主要讲了异常的继承,异常的抛出,else, finally
finally 无论如何都执行, try else则是没有异常就执行.

记:
RumtimeError -> Exception -> BaseException -> object


Flat is better than nested(扁平胜于嵌套)


## 关于三角形(aboutTriangleProject2)

test_illegal_triangles_throw_exceptions has expanded your awareness

## 总结
主要讲了异常的使用

*Although practicality beats purity.*
*实用大于完美*

## 关于iteration(about_iteration)

python 2 到python 3
把列表差不多都高成了迭代子形式
map ,filter,range,

1. test_iterators_are_a_type
2. test_iterating_with_next
3. test_map_transforrms_elements_of_a_list
4. test_just_return_first_item_found
5. test_reduce_will_blow_you_mind
6. test_use_pass_for_iterations_with_no_body
7. test_all_iteration_methods_work_on_any_sequence_not_joust_lists

### 总结
+ iter使用(1,2点),异常(StopIteration)
+ iter 转map,
+ reduce -> functools.reduce
+ iter for 结束后 i的值.




*In the face of ambiguity, refuse the temptation to guess.*
*碰到模棱两可的地方, 绝对不要去作猜测*



## 构造式(aboutComprehension)

1. test_creating_lists_with_list_comprehensions
2. test_filtering_lists_with_list_comprehensions
3. test_unpacking_tuples_in_list_comprehensions
4. test_double_list_comprehension
5. test_creating_a_set_with_set_comprehension
6. test_creating_a_dictionary_with_dictionary_comprehension

### 总结
构造式主要功能简化日常的操作,用几行代码实现多行代码的功能,
构造式主要包括,list,dict,tuple,dictionary


## 生成器(about_generators)

1. test_generating_values_on_the_fly
2. test_generators_are_different_to_list_comprehensions
3. test_generator_expressions_are_a_one_shot_deal
4. simple_generator_method
5. test_generator_method_will_yield_values_during_iteration
6. test_coroutines_can_take_arguments
7. test_generator_keeps_track_of_local_variables
8. test_generators_can_take_coroutines
9. test_generators_can_see_if_they_have_been_called_with_a_values
10. test_send_none_is_equivalent_to_next


### 总结
生成器与构造器的区别,生成器法则是用时再生,构造器是法则是全部一次性生成.
以括号表示,生成器有一个关健字,yield,yield是保侍当前环境并返回一个值,再次入时就是之前环境.
难点理解
yield ,next 和 send

一个协程的例子.

```
def yield_tester():
    value = yield # 1 在此挂起,等待next | send
    if value:
        yield value
    else:
        yield 'no value'

gen = yield_tester()
gen.next()

```

*If the implementation is easy to explain, it may be a good idea.*




### 应用是
1. 协程如gevent应该用了好多这个, send



## 关于lambda(aboutLambdas)

1. test_accessing_lambda_via_assignment
2. test_lambdas_can_be_assigned_to_variables_and_called_explicitly
3. test_accessing_lambda_without_assignment

### 总结

1. lambda 函数能分配给变量!
2. lambdas 函数能不用分配变量就可以调用!

*注意*
lambda 不用使用返回值!


*Namespaces are one honking great idea -- let's do more of those!*


## dice game(AboutScoringProject)

游戏规则

1. 3个1就是1000点,其他3个就是3 * X
2. 1 值就是100点(不属于3个以内)
3. 5 值就是50点(不属于3个以内)

例子

# Examples:
#
# score([1,1,1,5,1]) => 1150 points
# score([2,3,4,6,2]) => 0 points
# score([3,4,5,3,3]) => 350 points
# score([1,5,1,2,4]) => 250 points

解法

```

def score(dice):
    # You need to write this method
    total = 0
    one_total = dice.count(1)
    if one_total >= 3:
        total += 1000
        one_total -= 3
    total += one_total * 100

    for i in range(2, 7):
        if dice.count(i) >= 3:
            total += 100 * i
    if dice.count(5) > 3:
        total += (dice.count(5) - 3) * 50
    elif dice.count(5) < 3:
        total += dice.count(5) * 50

    return total


```

## 关于类(aboutClasses)

1. test_instances_of_classes_can_be_created_adding_parentheses
2. test_classes_have_docstrings
### 总结
fido.__class__.__name__
fido.__doc__

3. test_init_method_is_the_constructor
4. test_private_attributes_are_not_really_private
5. test_you_can_also_access_the_value_out_using_getattr_and_dict

### 总结
+ 类的初始化
+ 类的属性
+ 类的访问

6. test_that_name_can_be_read_as_a_property

+ 类的属性 可以使用

```

    class Dog3:

        def __init__(self):
            self._name = None

        def set_name(self, a_name):
            self._name = a_name

        def get_name(self):
            return self._name

        name = property(get_name, set_name)

```

7. test_creating_properties_with_decorators_is_slightly_easier

+ 属性令一种写法

```

   class Dog4:

        def __init__(self):
            self._name = None

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, a_name):
            self._name = a_name


```

8. test_inside_a_method_self_refers_to_the_containing_object
9. test_str_prpvides_a_string_version_of_the_object
10. test_all_objects_support_str_and_repr


### 总结
str 给终端用户看,repr 则是给开发者看
一切对象都有str和repr


## 关于with语句(about_with_statements)

1. test_counting_lines
2. test_finding_lines

### 用传统方法,计算行和发现行

```

       try:
            file = open(file_name)
            try:
                return len(file.readlines())
            finally:
                file.close()
        except IOError:
            # should never happen
            self.fail()


```


3. test_counting_lines2
4. test_finding_lines2

使用上下文管理器


```

    class FileContextManager():

        def __init__(self, file_name):
            self._file_name = file_name
            self._file = None

        def __enter__(self):
            self._file = open(self._file_name)
            return self._file

        def __exit__(self, cls, value, tb):
            self._file.close()

    # Now we write:

    def count_lines2(self, file_name):
        with self.FileContextManager(file_name) as file:
            return len(file.readlines())


```




5. test_finding_lines3

使用自定义的管理器

```

   def count_lines3(self, file_name):
        with open(file_name) as file:
            return len(file.readlines())

```

### 总结
Context managers are a way of allocating and releasing some sort of resource exactly where you need it.
上下文管理器是方便管理资源的开与关工具.


### 参考

[introduction-to-context-managers](http://eigenhombre.com/2013/04/20/introduction-to-context-managers/)



*If the implementation is easy to explain, it may be a good idea.*
*如果容易解释,这可能是一个好主意*


## 关于猴子补丁(about_monkey_patching)

![](http://7xnnj6.com1.z0.glb.clouddn.com/monkey.jpeg)


> A monkey patch is a way for a program to extend or modify supporting system software locally (affecting only the running instance of the program).

+ test_after_patching_dogs_can_both_wag_and_bark
+ test_most_built_in_classes_cannot_be_monkey_patched
+ test_subclasses_of_built_in_classes_can_be_be_monkey_patched

### 总结
可以添加方法到已经存在的类,但不可以添加到内建的方法.
*运行中*


```

class Dog:
    def bark(self):
        return "WOOF"

def wag(self):
    return "HAPPY"

Dog.wag = wag


```



## 关于骰子游戏


```

class DiceSet:

    def __init__(self):
        self._values = None

    @property
    def values(self):
        return self._values

    def roll(self, n):
        # Needs implementing!
        # Tip: random.randint(min, max) can be used to generate random numbers
        values = []
        for i in range(n):
            values.append(random.randint(1, 6))

        self._values = values


```


*Beautiful is better than ugly.*

*Readability counts.(可读性极具价值)*



## 关于方法绑定(about_method_bindings)

1. test_methods_are_bound_to_an_object
2. test_methods_are_also_bound_to_a_function


绑定用法

```

In [14]: class robot(object):
    def __init__(self,tip='welcome'):
        self.tip = tip
    def hello(self,name):
        print(self.tip,name)
   ....:

In [15]: r = robot()

In [16]: r.hello('lsl')
welcome lsl

In [17]: hello = r.hello

In [18]: hello('lsl')
welcome lsl




```

1. test_setting_attributes_on_an_unbound_function
2. test_setting_attributes_on_a_bound_method_directly

说明:函数能设置属性.


1. test_get_descriptor_resolves_attribute_binding
2. test_set_descriptor_changes_behavior_or_attribute_assignment_changes



```

    class BoundClass:

        def __get__(self, obj, cls):
            return (self, obj, cls)



    class SuperColor:

        def __init__(self):
            self.choice = None

        def __set__(self, obj, val):
            self.choice = val

```

说明:能通过修改set|get描述符改变类的默认行为.

### 技巧
1. 怎样判断方法是绑定,还是没绑定, hasattr(method, '__self__'), hasattr(method,'__func__')


### 总结
往函数中添加属性,这也许说明这就是唯一的.

### 记忆
__self__, __func__, __get__, __set__



## 关于函数装饰器(about_decorating_with_functions)


```

    def addcowbell(fn):
        fn.wow_factor = 'COWBELL BABY!'
        return fn

    @addcowbell
    def mediocre_song(self):
        return "o/~ We all live in a broken submarine o/~"

    def xmltag(fn):
        def func(*args):
            return '<' + fn(*args) + '/>'
        return func

    @xmltag
    def render_tag(self, name):
        return name


```

### 总结
装饰器作用是装饰,不能改变函数内部逻辑,也可以能,对参数进行修改!



*Errors should never pass silently.*


## 关于类装饰器(about_decorating_with_classes)

+ test_partial_that_wrappers_no_args
+ test_partial_that_wrappers_first_arg
+ test_partial_that_wrappers_al_args

```

max = functools.partial(max)
max(7,23)
max = functools.partial(max, 0)
max(-1)
max(99)
max = functools.partial(max, 99, 20)
max()


```
通过这个,能发现functools.partial重装定制函数的作用.


+ test_decorator_with_no_arguments

```

    class doubleit:

        def __init__(self, fn):
            self.fn = fn

        def __call__(self, *args):
            return self.fn(*args) + ', ' + self.fn(*args)

        def __get__(self, obj, cls=None):
            if not obj:
                # Decorating an unbound function
                return self
            else:
                # Decorating a bound method
                return functools.partial(self, obj)

    @doubleit
    def foo(self):
        return "foo"

```

总结: 显示类装饰器的用法!



```

    class documenter:

        def __init__(self, *args):
            self.fn_doc = args[0]

        def __call__(self, fn):
            def decorated_function(*args):
                return fn(*args)

            if fn.__doc__:
                decorated_function.__doc__ = fn.__doc__ + ": " + self.fn_doc
            else:
                decorated_function.__doc__ = self.fn_doc
            return decorated_function


    @documenter("Does nothing")
    def idler(self, num):
        "Idler"
        pass

```

+ test_documentor_which_already_has_a_docstring


总结:
文档在装饰器的位置!



## 参考
python-3.4.3-docs-html/library/string.html#formatspec
