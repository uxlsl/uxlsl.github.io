---
layout: post
title: scrapy之scrapyinghub简要使用笔记
category: 学习
keywords: 学习,2015
---

# 目标
部署到scrapyinghub上

# 步骤
必要准备

1. 在scrapyinghub注册,取得apikey[apikey][1]
2. 在scrapyinghub上建立scrapy项目取得project num 如 https://dash.scrapinghub.com/p/29986/jobs/,则project num是29986
3. 安装 shub ,使用pip install shub
4. 使用shub login, 填入apikey
5. 进入scrpy项目文件,配置scrapy.cfg
6. 部署 使用命令. shub deploy


``` scrapy.cfg配置示例

[deploy]
username = d267ffd3aaefe48b694fe231bf70fb400
project = 29986


```




# 技巧
可以使用命令行对scrapying的项目进行控制
比如:

shub deploy-egg --from-url https://github.com/scrapinghub/dateparser.git 63883
shub schedule myspider
shub items 1/1/1


# 参考

[apikey]: https://dash.scrapinghub.com/account/apikey
