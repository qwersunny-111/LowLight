import os
import cv2
from skimage.metrics import structural_similarity as ssim

def calculate_ssim(img1, img2):
    # 将图像转换为灰度
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # 计算SSIM
    score, _ = ssim(img1_gray, img2_gray, full=True)
    return score

def main(folder1, folder2, log_file="ssim_results_ourtrain.log"):
    # 列出两个文件夹中的图像文件
    images1 = sorted([f for f in os.listdir(folder1) if f.endswith(('.png', '.jpg', '.jpeg'))])
    images2 = sorted([f for f in os.listdir(folder2) if f.endswith(('.png', '.jpg', '.jpeg'))])
    
    # 确保两个文件夹的图像数量一致
    if len(images1) != len(images2):
        print("文件夹中的图像数量不一致")
        return

    total_ssim = 0
    pair_count = 0

    with open(log_file, "w") as log:
        log.write("Image Pair\t\tSSIM\n")
        log.write("="*30 + "\n")
        
        # 逐对读取图像并计算SSIM
        for img_name1, img_name2 in zip(images1, images2):
            img_path1 = os.path.join(folder1, img_name1)
            img_path2 = os.path.join(folder2, img_name2)
            
            img1 = cv2.imread(img_path1)
            img2 = cv2.imread(img_path2)
            
            if img1 is None or img2 is None:
                print(f"无法读取图像: {img_name1} 或 {img_name2}")
                continue
            
            # 计算SSIM并累加
            ssim_score = calculate_ssim(img1, img2)
            total_ssim += ssim_score
            pair_count += 1
            
            # 输出到.log文件
            log.write(f"{img_name1} vs {img_name2}\tSSIM: {ssim_score:.4f}\n")
            print(f"SSIM between {img_name1} and {img_name2}: {ssim_score:.4f}")

        # 计算平均SSIM
        avg_ssim = total_ssim / pair_count if pair_count > 0 else 0
        log.write("="*30 + "\n")
        log.write(f"Average SSIM: {avg_ssim:.4f}\n")
        print(f"Average SSIM: {avg_ssim:.4f}")

if __name__ == "__main__":
    folder1 = "/home/B_UserData/sunleyao/LowLight/test_data/image20241029"  # 替换为文件夹1的路径
    folder2 = "/home/B_UserData/sunleyao/LowLight/test_data/test_output_ourtrain_20241029"  # 替换为文件夹2的路径
    main(folder1, folder2)
