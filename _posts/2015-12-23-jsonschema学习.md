---
layout: post
title: jsonschema学习
category: 学习
keywords: 学习,2015
---

使用目的:是减轻检验数据的负担,能简则简

>  It’s just a declarative format for “describing the structure of other data”. This is both its strength and its weakness (which it shares with other similar schema languages). It is easy to concisely describe the surface structure of data, and automate validating data against it. However, since a JSON Schema can’t contain arbitrary code, there are certain constraints on the relationships between data elements that can’t be expressed. Any “validation tool” for a sufficiently complex data format, therefore, will likely have two phases of validation: one at the schema (or structural) level, and one at the semantic level. The latter check will likely need to be implemented using a more general-purpose programming language.

它是描述一个结构的数据的格式.


```

例子:

{
  "type": "object",
  "properties": {
    "first_name": { "type": "string" },
    "last_name": { "type": "string" },
    "birthday": { "type": "string", "format": "date-time" },
    "address": {
      "type": "object",
      "properties": {
        "street_address": { "type": "string" },
        "city": { "type": "string" },
        "state": { "type": "string" },
        "country": { "type" : "string" }
      }
    }
  }
}

```

# 技巧
用一个字典去表达一个对象及数值.


```

{ "type": "string" }

"I'm a string" # 对

42 # 错


```


# 难点 object表示
jsonschema object 表达dict

有四个主要属性

1. properties
2. additionalProperties
3. required
4. dependencies


```

{
  "type": "object",

  "properties": {
    "name": { "type": "string" },
    "credit_card": { "type": "number" }
  },

  "required": ["name"],

  "dependencies": {
    "credit_card": {
      "properties": {
        "billing_address": { "type": "string" }
      },
      "required": ["billing_address"]
    }
  }
}


{
  "name": "John Doe",
  "credit_card": 5555555555555555,
  "billing_address": "555 Debtor's Lane"
}



```


# 总结

使用jsonschema来表达json的结构,我觉得是可以,不好的是描述太大了,
一个简单的表达式,使用了好多行来表示,加上嵌套,有时觉得真的太难看明白了.


# 参考

[understanding json schema][]

[understanding json schema]: http://spacetelescope.github.io/understanding-json-schema/
