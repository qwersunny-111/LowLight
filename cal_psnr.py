import os
import cv2
import numpy as np

def calculate_psnr(img1, img2):
    # 计算均方误差 (MSE)
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return float('inf')  # 无差异时返回无限大
    # 计算 PSNR
    psnr = 20 * np.log10(255.0 / np.sqrt(mse))
    return psnr

def main(folder1, folder2, log_file="psnr_results_ourtrain.log"):
    # 列出两个文件夹中的图像文件
    images1 = sorted([f for f in os.listdir(folder1) if f.endswith(('.png', '.jpg', '.jpeg'))])
    images2 = sorted([f for f in os.listdir(folder2) if f.endswith(('.png', '.jpg', '.jpeg'))])
    
    # 确保两个文件夹的图像数量一致
    if len(images1) != len(images2):
        print("文件夹中的图像数量不一致")
        return

    total_psnr = 0
    pair_count = 0

    with open(log_file, "w") as log:
        log.write("Image Pair\t\tPSNR\n")
        log.write("="*30 + "\n")
        
        # 逐对读取图像并计算 PSNR
        for img_name1, img_name2 in zip(images1, images2):
            img_path1 = os.path.join(folder1, img_name1)
            img_path2 = os.path.join(folder2, img_name2)
            
            img1 = cv2.imread(img_path1)
            img2 = cv2.imread(img_path2)
            
            if img1 is None or img2 is None:
                print(f"无法读取图像: {img_name1} 或 {img_name2}")
                continue
            
            # 确保图像大小相同
            if img1.shape != img2.shape:
                print(f"图像尺寸不匹配: {img_name1} 和 {img_name2}")
                continue
            
            # 计算 PSNR 并累加
            psnr_score = calculate_psnr(img1, img2)
            total_psnr += psnr_score
            pair_count += 1
            
            # 输出到 .log 文件
            log.write(f"{img_name1} vs {img_name2}\tPSNR: {psnr_score:.4f}\n")
            print(f"PSNR between {img_name1} and {img_name2}: {psnr_score:.4f}")

        # 计算平均 PSNR
        avg_psnr = total_psnr / pair_count if pair_count > 0 else 0
        log.write("="*30 + "\n")
        log.write(f"Average PSNR: {avg_psnr:.4f}\n")
        print(f"Average PSNR: {avg_psnr:.4f}")

if __name__ == "__main__":
    folder1 = "/home/B_UserData/sunleyao/LowLight/test_data/image20241029"  # 替换为文件夹1的路径
    folder2 = "/home/B_UserData/sunleyao/LowLight/test_data/test_output_ourtrain_20241029"  # 替换为文件夹2的路径
    main(folder1, folder2)
