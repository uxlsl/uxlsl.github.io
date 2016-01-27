---
layout: post
title: python-koan 练习
category: 学习
keywords: 学习,2016
---

##  Python Koans - Learn Python through TDD


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


# emacs 技巧

1. M + %
2. C + W
editing
3. C + M + c
4. n

goto 2

# 关于字符串(about_string.py)

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

## 总结

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

### 技巧
1. 如果字符串中有',尽量使用",
2. 如果字符串中有",尽量使用',
3. 如果多行使用"""|'''

```

In [8]: 'hello' == "hello" == """hello"""
Out[8]: True


```

# 关于None

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


# 关于列表(about_list)

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

总结:
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

## range 负步长情况

range(5, 3, -1)


# 列表的赋值 (AboutListASSignments)

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


# 关于字典(about_dictionaries)

test_creating_dictionaries
test_dictionary_literals
test_accessing_dictionaries
test_changing_dictionaries
test_dictionary_is_unordered
test_dictionary_keys_and_values
test_making_a_dictionary_from_a_sequence_of_keys


总结:

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


# 字符串操作(AboutStringManipulation)

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

## 总结
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


# 元组(AboutTuples)
test_creating_a_tuple
test_tuples_are_imutable_so_item_assignment_is_not_possible
test_tuples_are_imutable_so_appending_is_not_possible
test_tuples_can_only_be_changed_through_replacement
test_tuples_of_one_look_peculiar
test_tuple_constructor_can_be_surprising
test_creating_empty_tuples
test_tuples_can_be_embedded
test_tuples_are_good_for_representing_records

## 总结

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



### 参考
python-3.4.3-docs-html/library/string.html#formatspec
