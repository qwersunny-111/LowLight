import os
from PIL import Image

# 原始图像文件夹路径
input_folder = '/home/B_UserData/sunleyao/LowLight/test_data/image20241029'
# 输出图像文件夹路径
output_folder = '/home/B_UserData/sunleyao/LowLight/test_data/resize20241029'

# 如果输出文件夹不存在，则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # 可以根据需要增加其他图像格式
        # 构建原始图像路径
        img_path = os.path.join(input_folder, filename)
        # 打开图像并调整大小
        img = Image.open(img_path)
        img_resized = img.resize((512, 512))
        # 构建输出图像路径并保存
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path)
        print(f"Saved resized image to {output_path}")

print("All images have been resized and saved.")
