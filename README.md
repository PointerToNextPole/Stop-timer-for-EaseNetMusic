​		写这个脚本的起因是：开始时使用的Win10平台，使用的音乐播放器是「网易云音乐」，因为在官网下载的网易云音乐客户端功能相当臃肿，而「网易云音乐WPF版」要简洁很多，所以一直在用「WPF版」。但「网易云音乐WPF版」没有「定时停止播放」功能，便自己用Python写了一个实现类似功能的很简易的脚本`closeNem.py`：运行Python脚本，调用控制台，输入继续播放的分钟数，以定时关闭网易云音乐。

​		命令模版：

```shell
python closeNem.py minNums
```

​		之后迁移到macOS平台后，便继续使用「网易云音乐 for Mac」，而「网易云音乐 for Mac」也没有「定时停止播放」功能，所以对原有脚本稍加修改了下，继续在Mac上使用，脚本名称仍为`closeNem.py`。

​		再后面，发现了自己有“到指定时间停止播放功能”的需求，便对代码进行了修改，脚本名称改成了`closeNem2.py`。添加了“到指定时间停止播放功能”功能，并添加了一些错误提示，以增加鲁棒性。

​		命令模版：

```shell
python3 closeNeM2.py minNums|hour:min
```



​		这个脚本写得很仓促，还有边角的问题没有发现，而且鲁棒性也并不怎么样。不过仅仅是自己用的，便偷了个懒，暂时没有进一步修改的意思。
