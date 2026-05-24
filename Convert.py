import os
import sys
import requests
from pdf2image import convert_from_bytes

def pdf_to_images_by_url(pdf_url, student_id):
    # 创建输出目录：images/学号
    output_dir = os.path.join("images", student_id)
    os.makedirs(output_dir, exist_ok=True)

    # 下载 PDF
    print(f"正在下载 PDF：{pdf_url}")
    response = requests.get(pdf_url, timeout=30)
    response.raise_for_status()

    # 转换 PDF 为图片
    print("正在将 PDF 转换为图片...")
    pages = convert_from_bytes(response.content, fmt="jpg")

    # 逐页保存，命名：页数_宽_高.jpg
    for i, page in enumerate(pages, 1):
        w, h = page.size
        filename = f"{i}_{w}_{h}.jpg"
        save_path = os.path.join(output_dir, filename)
        page.save(save_path, "JPEG")
        print(f"已保存：{save_path}")

    print(f"\n✅ 转换完成！共 {len(pages)} 页，保存路径：{output_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法：python Convert.py <PDF_URL> <学生学号>")
        sys.exit(1)

    pdf_url = sys.argv[1]
    student_id = sys.argv[2]
    pdf_to_images_by_url(pdf_url, student_id)
