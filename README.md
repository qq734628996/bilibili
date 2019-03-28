# bilibili

Extract the video of bilibili cache on the phone without loss.

将B站（[bilibili.com](bilibili.com)）缓存在手机上的视频无损提取出来。

## usage

需要安装[ffmpeg](http://ffmpeg.com/)。

B站在手机中的默认缓存路径为`Android/Data/tv.danmaku.bili/download/`，进去后可以看到av号，里面是对应的视频。

将手机里的缓存视频拷贝到电脑里面，运行

```python
python bilibili.py avpath
```

## demo

![](demo/demo.gif)