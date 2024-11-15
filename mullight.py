import os
from PIL import Image, ImageEnhance

# 输入文件夹路径（已修改分辨率的图像）
input_folder = '/home/B_UserData/sunleyao/LowLight/test_data/resize20241029'
# 输出文件夹路径（保存不同亮度版本的图像）
output_folder = '/home/B_UserData/sunleyao/LowLight/test_data/multilight20241029'

# 创建输出文件夹，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 定义不同亮度的系数（1.0 为原始亮度，低于 1.0 为降低亮度，高于 1.0 为增加亮度）
brightness_factors = [0.5, 0.8, 1.0, 1.2, 1.5]  # 可以根据需要调整这些系数

# 遍历输入文件夹中的所有图像文件
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # 为每个亮度系数生成不同的亮度版本
        for factor in brightness_factors:
            # 创建亮度增强器
            enhancer = ImageEnhance.Brightness(img)
            # 调整亮度
            img_bright = enhancer.enhance(factor)
            
            # 构建输出文件名，包含亮度系数
            output_filename = f"{os.path.splitext(filename)[0]}_brightness_{factor}.jpg"
            output_path = os.path.join(output_folder, output_filename)
            
            # 保存调整后的图像
            img_bright.save(output_path)
            print(f"Saved image with brightness factor {factor} to {output_path}")

print("All images have been processed with multiple brightness levels.")
