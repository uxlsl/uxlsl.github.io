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




# 关于字符串(about_string.py)

  test_adjacent_strings_are_concatenated_automatically has expanded your awareness.
  test_double_quoted_strings_are_strings has expanded your awareness.
  test_escaping_quotes_at_the_end_of_triple_quoted_string has expanded your awareness.
  test_most_strings_interpret_escape_characters has expanded your awareness.
  test_plus_concatenates_strings has expanded your awareness.
  test_plus_equals_also_leaves_original_string_unmodified has expanded your awareness.
  test_plus_equals_will_append_to_end_of_string has expanded your awareness.
  test_plus_will_not_modify_original_strings has expanded your awareness.
  test_raw_strings_are_also_strings has expanded your awareness.
  test_single_quoted_strings_are_also_strings has expanded your awareness.
  test_triple_quote_strings_are_also_strings has expanded your awareness.
  test_triple_quoted_strings_can_span_lines has expanded your awareness.
  test_triple_quoted_strings_need_less_escaping has expanded your awareness.
  test_triple_single_quotes_work_too has expanded your awareness.
  test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line has expanded your awareness.
  test_use_backslash_for_escaping_quotes_in_strings has expanded your awareness.
  test_use_double_quotes_to_create_strings_with_single_quotes has expanded your awareness.
  test_use_single_quotes_to_create_string_with_double_quotes has expanded your awareness.

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
