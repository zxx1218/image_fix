<h1><center>基于深度学习技术（Transformer、GAN）的专一或多类别图像修复算法（含GUI+Web端在线体验界面）</center></h1>

### 本篇文章是针对破损图片的修复。如果你想对灰度图片进行上色，或是老照片的色彩复原，请参考这篇CSDN作品👇

[基于深度学习的老（旧）照片上色算法模型设计与实现（对抗生成式网络GAN、含Github代码与Web端设计）](https://blog.csdn.net/qq_45566099/article/details/138611013)

### 如果要做老照片色彩增强，清晰化，请参考这篇CSDN作品👇

[计算机毕业设计--老照片（灰白照片）清晰化+划痕修复+色彩增强的深度学习算法设计与实现（含giuhub代码+GUI可视化界面）](https://blog.csdn.net/qq_45566099/article/details/136506388)

<h3><center>更多基于深度学习的毕业设计请关注专栏 --- <a href="http://t.csdnimg.cn/ZTAtt">计算机毕业设计</a></center></h3>
<hr>https://blog.csdn.net/qq_45566099/article/details/136506388)

## :sparkles: 人脸修复Demo（模型训练基于CelebA-HQ数据集 - 4万张图）

<img src="./show_img/csdn展示图.jpg" width="1000px">

## :sparkles: 建筑&风景修复Demo（模型训练基于Places2数据集 - 180万张图）

- 稍后上传



## :sparkles: 图像修复在线体验

👇
 **Web端在线体验地址：**:white_check_mark:[访问这里进行图像修复在线体验](http://qh880639rv62.vicp.fun):white_check_mark:

**在线体验地址已经集成了训练好的模型，您只需点击选择使用的模型即可！**

:package:：训练人脸修复模型的数据集“CelebA-HQ”在这里下载（也可以换用其他图片进行测试，但选择使用数据集中的4万张图进行测试效果最好）

```
百度网盘分享的文件
链接：https://pan.baidu.com/s/1f8v6-OQsK_6YHvlvTvovGQ?pwd=khgb 
提取码：khgb
```

:package:：用于辅助图片修复的Mask在这里下载（必须使用Mask，Mask的作用是告知模型图片破损的位置）

```
百度网盘分享的文件
链接：https://pan.baidu.com/s/1Det77BagB6Xm3LdKG1_JFA?pwd=zz1k 
提取码：zz1k
```



**在线体验使用方式：**
&emsp;&emsp;打开连接后，左侧两个图片输入框分别需要上传待修复的原图和代表原图上破损位置的Mask。**在网页下方提供了四组输入样例，点击样例自动填充到相应位置后即可点击开始修复查看效果。**

**注意：** 修复第一张图的时候耗时较长，大约10秒左右。从第二张图开始，速度就会快起来，大约5秒左右一张（这主要是因为第一次启动的时候模型需要加载进显卡中）



<img src="./show_img/gradio展示1.png" width="900px">

<img src="./show_img/gradio展示2.png" width="900px">

<hr>




  ## 模型研究背景

&emsp;&emsp;在图像获取和传输过程中，往往伴随着各种形式的损坏，降低了图像质量和对图像信息的准确解释，一些老照片因为保存不当也会变得存在污渍或者破损缺失。图像修复技术主要用来修复日常生活中被噪声污染或者人为破坏的破损图像，也可应用于替换图像中的小区域或者瑕疵。目前，图像修复工作仍然由经验丰富的图像修复师来完成，让图像修复借助深度学习算法实现自动化日趋成为该领域的发展方向。本课题基于深度学习算法和图像处理技术，设计并开发一款图像修复深度学习算法程序，该算法能够对使用者上传的照片进行自动化分析，修复照片的损坏部分，提高照片的清晰度和观赏性。

## 模型介绍

&emsp;&emsp;最近的研究表明，在图像修复问题中建立远程相互作用模型具有很高的重要性。为了实现这一目标，现有的方法要么利用独立注意力技术，要么利用Transformer。但是，考虑到计算成本，并且通常需要修复低分辨率下的图像。本课题提出了一种新的基于Transformer的图像修复模型，该模型能够有效处理高分辨率图像。具体来说，本课题设计了一个面向预测像素的Transformer结构模型，结合卷积的上下采样和图像风格迁移技术来实现缺失或者模糊图像的修复。
&emsp;&emsp;模型由卷积头、GAN模块、Transformer模块、卷积尾和风格迁移模块组成。 卷积头负责从输入图像和掩码中提取视觉标记。它包括四个3*3卷积，用于更改图像维度和下采样。GAN和Transformer是模型的主要组成部分，由五个不同分辨率的Transformer组成（内嵌五对GAN编解码器）从而使用多头情境注意力对长距离互动进行建模。 卷积尾用于对输出标记的空间分辨率进行上采样以匹配输入大小。风格迁移模块旨在实现多元化生成并增强输出的多样性，它通过使用额外的噪声输入在重建过程中更改卷积层的权重归一化来操纵输出。此外，该模块还结合了图像条件样式和无噪声样式，以增强噪声输入的表示能力。

## 模型性能指标测试

- 包括SSIM（Structural Similarity）结构相似性指标、PSNR（Peak signal-to-noise ratio） 峰值信噪比指标以及PID、UID指标的评估，如需测试数据或需要在自训练模型上完成指标测试，请联系作者（联系方式见文末）



<hr>


  ## :rocket: 运行要求

- 运行算法与Web前端需要 Python >= 3.8
- 运行GUI界面需要下载Qt Create编译器 5.14.2 版本
- 我提供在 CelebA-HQ 和 Places2 数据集训练好的两个模型，建议使用带有Nvidia（英伟达）系列的显卡（例如常见的GeForce 1060、3050、3090、4090等都是Nvidia系列的）
- **如果电脑没有合适的显卡也可使用该模型（需通过内存加载模型并丢给CPU进行推理计算，推理速度会慢很多）**



<hr>



  ## :zap:模型所需环境配置及使用方法（Windows / Linux 均适用）

  ### 环境配置

#### 方式一：使用conda安装环境

  ```
# 从github上Clone项目（需要你安装了git工具）
git clone https://github.com/zxx1218/image_fix.git

# 使用conda创建环境
conda create -n imgfix python=3.8
conda activate imgfix 

# 安装依赖
pip install -r requirements.txt 
  ```

#### 方式二：使用Docker

```
# 联系作者咨询，联系方式在文末
```



### 算法模型使用

#### 方式一：启动Web端应用（Web端框架自带移动端页面自适应）

 **\* 效果同上述在线体验连接**

   启动web端（会启动在127.0.0.1:xxxx的本机环回地址下)

  ```
python gradio_demo.py
  ```

回车后会自动启动Web服务，在控制台看到如下信息代表成功启动，在浏览器打开弹出的URL即可👇

  <img src="./show_img/gradio_kzt.png" width="900px">

**注：项目也支持进行基于Python的FastApi后端服务部署（针对Web服务器部署）。如有需要，联系作者，联系方式在文末**



#### 方式二：启动基于QT的桌面应用（支持打包发布为桌面.exe可执行文件）

使用Qt Create编译器运行QT代码即可直接使用（SQLlite数据库为代码内嵌，无需特别配置），启动后首先经过注册与登录界面，登录后效果如下图

- 上传mask位置有用户选择mask后，会自动覆盖在原图上，并显示为原图覆盖mask后的结果）
- 设计了根据不同登录用户的用户历史修图记录查询功能



<img src="./show_img/Snipaste_2024-06-04_09-59-19.png" width="700px">

#### 方式三：大批量图像批量修复（通过控制台 / cmd / 终端）

  执行如下命令：

```
# 首先cd到算法代码imf_fix根目录下
cd img_fix

# 将待修复图片放在指定文件夹

# 执行generate_image_cpu.py文件（这里需要根据修复需求添加相关参数）
python generate_image_cpu.py
```

控制台显示如下日志信息代表批量修图成功👇

  <img src="./show_img/cmd_demo.png" width="500px">

  <hr>



  ## 算法模型使用演示视频（桌面应用 & Web前端 & 控制台）

  ### 1. 通过GUI进行图像修复

  视频中上传的黑白图中黑色部分代表图片的破损位置（V2.0版本中上传的mask会覆盖在原图上进行显示。视频中演示的是V1.0版本），模型会将黑白图完全覆盖在原图上通过未破损位置对破损位置进行修复

  - 由于github上传视频受限，观看演示视频请移步至我的CSDN观看，连接：https://blog.csdn.net/qq_45566099/article/details/134942373

  PS：2024.6.4 QT界面已经升级到V2.0版本，提供了内嵌的sellite轻量级数据库支持（无需配置版的数据库）以及GUI界面的美化（主要为mask上传后显示为在原图上的覆盖），并添加了历史记录查询功能。

  ### 2. 访问Web进行图像修复

Web端在线体验地址：:white_check_mark:[访问这里进行图像修复在线体验](http://qh880639rv62.vicp.fun):white_check_mark:

  - 由于github上传视频受限，观看演示视频请移步至我的CSDN观看，连接：https://blog.csdn.net/qq_45566099/article/details/134942373

  ### 3. 通过控制台（cmd \ 终端）直接调用模型进行图像批量修复（一次性修复若干张图）：

  - 由于github上传视频受限，观看演示视频请移步至我的CSDN观看，连接：https://blog.csdn.net/qq_45566099/article/details/134942373

  <hr>



  ## :wrench:	如何自己训练模型?

- 训练自己想要的定制化图像修复模型**只需要准备好针对需要修复图片的同类型图片数据即可**，具体训练方式请咨询作者

  <hr>

## 作者联系方式：

- **VX：Accddvva**
- **QQ：1144968929**
- Github提供训练好的模型文件以及调用该文件进行修图的测试代码（**Github开源代码中不含模型定义源码、训练代码以及QT的桌面端GUI代码，提供可供测试的模型文件，拉取Git代码后安装环境可进行修图测试**）
- 该项目完整代码 + 详细环境配置（如有需要可提供模型远程部署）+ GUI界面 + Web端 + 训练方式 == 价格300RMB
- 如果你的电脑没有合适的GPU，或需要自行训练私有数据而自己的GPU现存或性能不够，作者另提供GPU服务器短期租赁服务，24G显存+64G内存云服务器每周 100RMB

<hr>


## 一些模型训练可用的公开数据集

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

- 作者于浙江某985高校就读人工智能方向研究生，可以帮忙定制设计模型，并提供代码和训练后的模型文件以及环境配置和使用方法，只需要描述需求即可
- 人工智能领域，尤其是计算机视觉（Computer vision，CV）方向的模型or毕业设计，只要你想得出，没有做不出的
