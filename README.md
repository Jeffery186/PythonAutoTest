# PythonAutoTest

## 环境要求

**驱动**

https://sites.google.com/a/chromium.org/chromedriver/downloads

https://npm.taobao.org/mirrors/chromedriver/

```bash
Python 3.8.7
Selenium 3.141.0
Google Chrome 90.0.4430.93
https://npm.taobao.org/mirrors/chromedriver/90.0.4430.24/
```

```bash
pip install selenium==3.141.0
pip install pytest==6.2.3
pip install pytest-html==3.1.1
pip install pytest-rerunfailures==9.1.1
pip install pytest-xdist==2.2.1
```

注：依赖目前是这些版本，使用时可以安装最新版的，如果报错可以适当修改代码以兼容新版(或者再手动安装上面指定的版本)。

## 开始

```bash
git clone https://github.com/zyhibook/PythonAutoTest.git
cd PythonAutoTest\pytest\Examples
```

然后直接运行`run.py`

```bash
python run.py
```

运行之后会在当前工作目录自动创建`allure-results`、`allure-reports`两个文件夹，前者是测试结果数据，后者是allure测试报告。

## 集成到Jenkins

集成到Jenkins比较简单，这里不再赘述。

## 其它相关

### Python下载

https://www.python.org/downloads/

### pypi 镜像

#### 设为默认

升级 pip 到最新的版本 (>=10.0.0) 后进行配置：

```
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

如果您到 pip 默认源的网络连接较差，临时使用本镜像站来升级 pip：

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
```

#### 腾讯源可以作为备用

https://mirrors.cloud.tencent.com/

## 代码目录结构

![](https://www.imglink.cc/images/2021/05/03/2129f1a4828af5a9394dafb87a4e80d2.png)

## 生成allure测试报告效果

![](https://www.imglink.cc/images/2021/05/03/6ad2892ce52152b4861e7f54bd93d7ee.png)

------

参考资料：

https://www.selenium.dev/documentation/zh-cn/

https://github.com/SeleniumHQ/selenium

> 自动化测试主要用于回归测试

