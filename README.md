# bilibili

Extract the video of bilibili cache on the phone without loss.

将B站（[bilibili.com](bilibili.com)）缓存在手机上的视频无损提取出来。

## Usage

需要安装[ffmpeg](http://ffmpeg.com/)，Windows请自行到官网下载，并配置环境变量或者将`ffmpeg.exe`置于`bilibili.py`相同路径下；linux和unix安装ffmpeg，例如Ubuntu：

```shell
$ apt install ffmpeg
```

B站在手机中的默认缓存路径为`Android\data\tv.danmaku.bili\download`，进去后可以看到av号，里面是对应的视频。

将手机里的缓存视频拷贝到电脑里面，运行

```shell
python bilibili.py avpath
```

## Demo

![alt text](demo/demo.gif)