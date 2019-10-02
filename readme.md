# 后端

## API

### 概览

```
register/ : 注册
login/ : 登录
validate/ : 用于邮箱验证
```

### 注册

```
register/
POST方式，参数如下：

username: 用户名，需要唯一，仅允许大小写字母、下划线和数字
password: 密码，长度不低于8位，不长于20位
email: 邮箱，需要验证之后才能使用
```

## 数据库

### User 类

TODO

```
username: 用户名
password: 密码
email: 邮箱
valid: 邮箱是否验证

```

### Email 类

TODO
