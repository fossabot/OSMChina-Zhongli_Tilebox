# TileRequest

## 功能

可以下载指定等级下，固定范围或全图的瓦片

## 测试用例

```python
taskGenerator(0, "OSMChina", "测试任务S", "Full")
taskGenerator(2, "OSMChina", "测试任务R", "Region", 2, 3, 2, 3)
taskGenerator(3, "OSMChina", "测试任务F", "Full")
```