---
layout: post
title: jquery插件的使用的例子
category: 学习
keywords: 学习,2015
---

# jquery插件的使用的例子

![jquery插件](http://7xnnj6.com1.z0.glb.clouddn.com/jquery_form_validation.png)


**说明**

使用jquery.validate.js来检验表格输入是否符合要求,
使用jquery.form.js来实现ajax表格.

**总结**
jquery.validate.js使用步骤
1. 引入jquery.validate.js
2. 对表格要检验的表使用 $("XXX").validate(),XXX为选择表达式.
3. 对于校难的使用 class装饰.

jquery.form.js使用步骤
1. 引入jquery.form.js
2. 写options
3. 调用ajaxform方法

## 参考

[官网](http://jqueryvalidation.org)
[marketo](http://jqueryvalidation.org/files/demo/marketo/)
[jquery.form实例](http://jquery.malsup.com/form/#ajaxForm)

## 自己写的例子

```

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>表单提交与表格操作的插件例子</title>
    <!-- 引入 jQuery -->
    <script src="./scripts/jquery.js" type="text/javascript"></script>
    <script src="./scripts/jquery.form.js" type="text/javascript"></script>
    <script src="./scripts/jquery.validate.js" type="text/javascript"></script>
    <script type="text/javascript">
  $(document).ready(function(){
    $(".cmxform").validate();
    var options = {
      dataType: "json",
      success:function(data){
        $("tbody:eq(1) tr").remove();
        for (var i=0; i < data.length; i++){
          var $l = $("<tr>" +
                     "<td>" + data[i]["name"] + "</td>" +
                     "<td>" + data[i]["age"] + "</td>" +
                     "<td>" + data[i]["updated_at"] + "</td>"+
                     "</tr>");
          $("tbody:eq(1)").append($l);
        }
      },
      timeout: 3000,
    }
    $("form").ajaxForm(options);
  })
   </script>
  </head>
  <body>
    <form class="cmxform" action="/people" method="get">
      <input type="text" name="name" size="25" class="required" minlength="1">
      <input type="submit" value="Submit" />
      </form >
      <table border="1">
        <tbody>
        <tr>
          <td>姓名</td>
          <td>年龄</td>
          <td>更新时间</td>
        </tr>
        </tbody>
        <tbody>
        <tr>
          <td>lsl</td>
          <td>27</td>
          <td>2012.11.11</td>
        </tr>
        </tbody>
      </table>
  </body>
</html>


```
