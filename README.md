# 基于深度学习技术（Transformer、GAN）的图像修复算法（含Github代码+GUI桌面应用程序与Web端界面代码）

### 本篇文章是针对破损照片的修复。如果你想对老照片进行灰度图上色，色彩复原，请参考这篇CSDN作品（含Github代码）👇

[基于深度学习的老（旧）照片上色算法模型设计与实现（对抗生成式网络GAN、含Github代码与Web端设计）](https://blog.csdn.net/qq_45566099/article/details/138611013)

### 如果要做老照片色彩增强，清晰化，划痕修复，划痕检测，请参考这篇CSDN作品（含Github代码）👇

[计算机毕业设计--老照片（灰白照片）清晰化+划痕修复+色彩增强的深度学习算法设计与实现（含giuhub代码+GUI可视化界面）](https://blog.csdn.net/qq_45566099/article/details/136506388)

## :sparkles: 人脸修复Demo（模型训练基于CelebA-HQ数据集 - 4万张图）

<img src="./show_img/csdn展示图.jpg" width="1000px">

## :sparkles: 建筑&风景修复Demo（模型训练基于Places2数据集 - 180万张图）

- 稍后上传

## :sparkles: 网页端效果展示

👇
**Web端在线体验地址：**:white_check_mark:[访问这里进行图像修复在线体验](https://qh880639rv62.vicp.fun/):white_check_mark:

PS：用于人脸修复的数据集在这里下载（也可以换用其他图片，但使用CelebA-HQ中的4万张图进行测试效果最好）

```
百度网盘分享的文件
链接：https://pan.baidu.com/s/1f8v6-OQsK_6YHvlvTvovGQ?pwd=khgb 
提取码：khgb
```

PS：用于图片修复的Mask在这里下载（必须使用Mask，Mask的作用是告知模型图片破损的位置）

```
百度网盘分享的文件
链接：https://pan.baidu.com/s/1Det77BagB6Xm3LdKG1_JFA?pwd=zz1k 
提取码：zz1k
```

👆

<img src="./show_img/gradio展示.png" width="900px">

<hr>




## 研究背景

&emsp;&emsp;在图像获取和传输过程中，往往伴随着各种形式的损坏，降低了图像质量和对图像信息的准确解释，一些老照片因为保存不当也会变得存在污渍或者破损缺失。图像修复技术主要用来修复日常生活中被噪声污染或者人为破坏的破损图像，也可应用于替换图像中的小区域或者瑕疵。目前，图像修复工作仍然由经验丰富的图像修复师来完成，让图像修复借助深度学习算法实现自动化日趋成为该领域的发展方向。本课题基于深度学习算法和图像处理技术，设计并开发一款图像修复深度学习算法程序，该算法能够对使用者上传的照片进行自动化分析，修复照片的损坏部分，提高照片的清晰度和观赏性。

## 介绍

&emsp;&emsp;最近的研究表明，在图像修复问题中建立远程相互作用模型具有很高的重要性。为了实现这一目标，现有的方法要么利用独立注意力技术，要么利用Transformer。但是，考虑到计算成本，并且通常需要修复低分辨率下的图像。本课题提出了一种新的基于Transformer的图像修复模型，该模型能够有效处理高分辨率图像。具体来说，本课题设计了一个面向预测像素的Transformer结构模型，结合卷积的上下采样和图像风格迁移技术来实现缺失或者模糊图像的修复。
&emsp;&emsp;该模型由以下几个主要部分组成：卷积头、Transformer、卷积尾和风格迁移模块。 卷积头负责从输入图像和掩码中提取视觉标记。它包括四个3*3卷积层，用于更改图像维度和下采样。Transformer是模型的主要组成部分，由五个不同分辨率的Transformer组成。使用多头情境注意力对长距离互动进行建模。 卷积尾用于对输出标记的空间分辨率进行上采样以匹配输入大小。风格迁移模块旨在实现多元化生成并增强输出的多样性。它通过使用额外的噪声输入在重建过程中更改卷积层的权重归一化来操纵输出。该模块还结合了图像条件样式和无噪声样式，以增强噪声输入的表示能力。

## 指标测试&结果

- 待作者整理后上传



<img src="./show_img/模型结构图.png" width="1000px">

<hr>


## :rocket: 运行要求

- 运行算法与Web前端需要 Python >= 3.8
- 运行GUI界面需要下载QT编译器 5.14.2 版本
- 我提供在 CelebA-HQ 和 Places2 数据集训练好的两个模型，建议使用带有nvidia系列的显卡（比如说RTX1060、3060、4090等等都是nvidia系列的显卡）
- 如果电脑没有显卡也可以直接调用该模型（通过CPU+内存加载模型）

<hr>



## :zap:开始

### 环境配置（推荐使用conda安装环境）

```
# Clone项目
git clone https://github.com/zxx1218/image_fix.git

# 使用conda创建环境
conda create -n imgfix python=3.8
conda activate imgfix 

# 安装依赖
pip install -r requirements.txt 
```

### 方式一：启动Web端交互界面

 启动web端（会启动在127.0.0.1:xxxx的本机环回地址下)

```
python gradio_demo.py
```

回车后会自动启动Web服务，在控制台看到如下信息代表成功启动，在浏览器打开弹出的URL即可👇

<img src="./show_img/gradio_kzt.png" width="900px">

### 方式二：启动基于QT的桌面应用GUI

使用QT编译器打开QT代码即可，详见[计算机毕业设计--基于深度学习技术（Transformer、GAN）的破损图像修复算法（含Github代码+GUI与Web端展示界面）_计算机专业本科毕业设计深度学习-CSDN博客](https://blog.csdn.net/qq_45566099/article/details/134942373)

<img src="./show_img/Snipaste_2024-06-04_09-59-19.png" width="800px">

### 方式三：通过控制台（cmd \ 终端）进行批量修复

按照下述操作执行：

```
# 首先cd到算法代码imf_fix根目录下
cd img_fix

# 执行generate_image_cpu.py文件（这里需要根据修复需求添加相关参数）
python generate_image_cpu.py
```

回车后，会在控制台看到如下日志信息👇

<img src="./show_img/cmd_demo.png" width="500px">

<hr>


## 模型演示（控制台演示 & QT界面展示）

### 1. 通过GUI进行图像修复

视频中上传的黑白图中黑色部分代表图片的破损位置（V2.0版本中上传的mask会覆盖在原图上进行显示。视频中演示的是V1.0版本），模型会将黑白图完全覆盖在原图上通过未破损位置对破损位置进行修复

- 由于github上传视频受限，观看演示视频请移步至我的CSDN观看，连接：https://blog.csdn.net/qq_45566099/article/details/134942373

PS：2024.6.4 QT界面已经升级到V2.0版本，提供了内嵌的sellite轻量级数据库支持（无需配置版的数据库）以及GUI界面的美化（主要为mask上传后显示为在原图上的覆盖），并添加了历史记录查询功能。

### 2. 访问Web进行图像修复

Web端在线体验地址： :white_check_mark:[访问这里进行图像修复在线体验](https://qh880639rv62.vicp.fun/):white_check_mark:

- 由于github上传视频受限，观看演示视频请移步至我的CSDN观看，连接：https://blog.csdn.net/qq_45566099/article/details/134942373

### 3. 通过控制台（cmd \ 终端）直接调用模型进行图像批量修复（一次性修复若干张图）：

- 由于github上传视频受限，观看演示视频请移步至我的CSDN观看，连接：https://blog.csdn.net/qq_45566099/article/details/134942373

<hr>


## :wrench:	如何自己训练模型?

- 项目提供自行训练or微调的方式，请咨询作者



## 作者联系方式：

- VX：Accddvva
- QQ：1144968929

- Github提供训练好的模型文件以及调用该文件进行修图的测试代码（clone代码后安装环境即可进行修图测试，开源版不包含模型源码以及gui）
- 本项目完整代码 + 环境配置方法（另可提供远程部署服务）+ GUI界面 + Web端 == **价格300RMB，可提供远程部署服务，另提供GPU服务器短期租赁服务，24G显存服务器每个月100RMB**

<hr>


## 模型训练可用公开数据集

- **人脸（提供训练过的模型文件）**公开数据集**CelebA-HQ**：链接：https://github.com/tkarras/progressive_growing_of_gans
  制作机构：Tero Karras, Samuli Laine, Timo Aila 和 NVIDIA 的研究人员制作-内含约4万张训练图片
- **自然场景（提供训练过的模型文件）**公开数据集**Places2**：链接：http://places2.csail.mit.edu/download.html
  制作机构：斯坦福大学和微软研究院共同制作-内含180万张训练图片
- **街景**公开数据集**Paris StreetView**：链接：http://opendata.paris.fr/explore/dataset/photos-de-rue-a-paris/
  制作机构：巴黎市政府
- **文理**公开数据集**DTD**：链接：http://www.robots.ox.ac.uk/~vgg/data/dtd/。
  制作机构：英国牛津大学计算机视觉研究团队
- **建筑**公开数据集**Façade**：链接：
  GitHub上的项目：https://github.com/shannontian/facade-parsing
  官方网站：CMP Facade Database
  数据集共享平台：https://www.vision.ee.ethz.ch/datasets_extra/facade/
  制作机构：Czech Technical University in Prague (捷克技术大学)

<hr>


## 广告

- 作者于浙江某985高校就读人工智能方向研究生，可以帮忙定制设计模型，并提供源代码和训练后的模型文件以及环境配置和使用方法，只需要描述需求即可。
- 人工智能领域，尤其是计算机视觉（Computer vision，CV）方向的毕业设计，只要你想得出，没有做不出的
