# TileTool

## 承诺

OSMChina承诺

本项目可且仅可用于爬取OSMChina自有的瓦片服务。

不提供对其他非自有瓦片服务的爬取并屏蔽对外来源。

该工具仅用于诊断和调试渲染风格使用。

## 功能

**XXX，Anti的就是Universal MD**

1. TileTool.Request

   可以下载指定等级下，固定范围或全图的瓦片

2. TileTool.Combiner

   可以把一堆瓦片合并

3. TileTool.Viewer

   可以直接查看瓦片

## 测试用例

```python
taskGenerator(0, "OSMChina", "测试任务S", "Full")
taskGenerator(2, "OSMChina", "测试任务R", "Region", 2, 3, 2, 3)
taskGenerator(3, "OSMChina", "测试任务F", "Full")
```

TODO

1. 多线程
2. 多样化的请求顺序（随机压测或者中心辐射，多中心同步辐射）
2. Combiner & Viewer
3. 允许重启后继续进度（或者可能搞成一种专有格式）
4. 

这个与[github.com/AMDmi3/tiletool](https://wiki.openstreetmap.org/wiki/Tiletool)不是一回事，但他的功能我们可以学习
