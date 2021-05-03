# pytest

## 注意事项

```bash
1.测试类以Test开头，并目不能带有init方法
2.测试文件必须以test_开头(或者以_test结尾)
3.测试函数必须以test_开头
```

### 执行

#### 法1：

```bash
main pytest.main
```

代码：

```python
# 执行
if __name__ == '__main__':
    pytest.main()
```

指定执行用例：

```python
# 执行
if __name__ == '__main__':
    pytest.main(['-s','test_0.py'])
```

`-s`：打印输出结果

`'test_0.py'`：指定执行用例

#### 法2：

终端中执行

```bash
pytest
```

![](https://www.imglink.cc/images/2021/05/03/f34f1e02420eb17a1516890d2be32933.png)

## 官方文档

https://docs.pytest.org/

