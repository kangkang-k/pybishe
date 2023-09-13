数据库配置

安装 `pymysql`

在`settings.py` 中找到

DATABASES 

然后修改为自己得

```python
DATABASES = { 
    'default': 
    { 
        'ENGINE': 'django.db.backends.mysql',    # 数据库引擎
        'NAME': 'runoob', # 数据库名称
        'HOST': '127.0.0.1', # 数据库地址，本机 ip 地址 127.0.0.1 
        'PORT': 3306, # 端口 
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123456', # 数据库密码
    }  
}
```

```
# 在与 settings.py 同级目录下的 __init__.py 中引入模块和进行配置
import pymysql
pymysql.install_as_MySQLdb()
```



生成一个实体类模块

```
django-admin startapp 模块名称
```

models.py 就是我们的实体类

```python
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)
```

类名对应数据库名称



然后 在 settings.py  INSTALLED_APPS这一项

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TestModel',               # 添加此项  模块名称
)
```



```shell
python manage.py migrate  # 创建表结构
python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
python manage.py migrate TestModel  # 创建表结构
```

> python manage.py  makemigrations --empty teacher

保存数据

```python
# 内置方法 创建我们的对象
test1 = Test(name='zs')
test1.save()
```



查询

```python
# 查询全部
list = Test.objects.all()
# 添加过滤添加
Test.objects.filter(id=1) 

# 获取单个对象
response3 = Test.objects.get(id=1) 

# 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
Test.objects.order_by('name')[0:2]

#数据排序
Test.objects.order_by("id")

# 上面的方法可以连锁使用
Test.objects.filter(name="runoob").order_by("id")
```



修改

```python
# 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()
    
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')
```



接收参数

```python
resp = {'errorcode': 100, 'detail': 'Get success'}
return HttpResponse(json.dumps(resp), content_type="application/json")
```

