from PIL import Image

# 打开图片
image = Image.open('/home/zxx/zxxCode/MAT-main/test_sets/my/images/010264.jpg')

# 调整图片大小
resized_image = image.resize((512, 512))

# 旋转图片
fixed_image = resized_image.rotate(180) # 如果缩放后的图片颠倒了，那么就启用这句话

# 保存调整后的图片
resized_image.save('/home/zxx/zxxCode/MAT-main/test_sets/my/images/010264.jpg')