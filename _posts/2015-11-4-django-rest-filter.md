---
layout: post
title: django-rest-filter小结
category: python
keywords: 阅读,2015
---

# django-filter小结

## django-filter 是什么?

Django-filter is a reusable Django application for allowing users to filter querysets dynamically.
(是一个可重用的django应用,能够动态的过滤queryset)
处理的层是参数输入与过滤数据这一层

##　为什么要使用这个?
解决了多次重写过滤数据这一环节,在这一环节要考虑的问题是
+ 参数是否有输入
+ 是如何匹配

## django-rest-framework为什么要使用?

ViewSet　默认不提供过滤,　过滤的是pk, list是列表全部.


## 例子

```

    import django_filters

    class ProductFilter(django_filters.FilterSet):
        class Meta:
            model = Product
            fields = ['name', 'price', 'manufacturer']

    def product_list(request):
        filter = ProductFilter(request.GET, queryset=Product.objects.all())
        return render_to_response('my_app/template.html', {'filter': filter})



```

django-rest-framework 的示例


```

    class FooFilter(django_filters.FilterSet):

        class Meta:
            model = StockDetail
            fields = {
                "warehouse_id": ["exact"],
                "business_type": ["exact"],
                "business_no": ["exact"],
                "status_id": ["exact"],
                "sku_id": ["exact"],
                "operation_time": ["exact", "gte", "lte"]
            }
            order_by = ['operation_time']


    class FooView(ListAPIView):
        queryset = Foo.objects.all()
        serializer_class = FooSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        filter_class = FooFilter


```
