# 基于 Socket 的 Web Server

简介
----

- 基于 Socket 进行通信， 解析 HTTP 协议，构建完整的 Web Server
- 采用 MVC 架构，实现数据与页面的分离， 提高代码的可复用性
- Model 层使用基于 MySQL 的 ORM，实现了 MySQL 增删改查接口的封装
- View 层使用 Jinja2 模板语言，通过模板生成 HTML 代码
- Controller 层由自制的 Web 框架实现，实现了 HTTP 请求解析、注册路由与路由函数映射、HTTP 响应数据 API
- 实现用户管理功能，包括注册、登录、密码 加盐 保护、Session 管理和 权限 管理等功能

依赖
-----

- Python 3
- MySQL
- Jinja2

如何运行
---------

- 需要您在根目录下自行添加 `secret.py` 文件，内容为：
```
mysql_password = 'your password'
db_name = 'your db_name'
```
- 运行 `reset.py` 
- 运行 `server.py`

功能演示
--------

- 注册

![注册](https://github.com/Caizt/Web-Server/blob/master/static/weibo1.gif)

- 登录

![登录](https://github.com/Caizt/Web-Server/blob/master/static/weibo2.gif)

- 编辑、删除微博和评论

![编辑、删除微博和评论](https://github.com/Caizt/Web-Server/blob/master/static/weibo3.gif)
