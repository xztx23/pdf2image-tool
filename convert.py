import os
import requests
from pdf2image import convert_from_bytes

# 从环境变量读取参数（和你的run.yml完全匹配）
pdf_url = os.environ.get("PDF_URL")
student_id = os.environ.get("STUDENT_ID")

# 自动检查并创建文件夹
if not os.path.exists("images"):
    os.makedirs("images")

save_dir = f"images/{student_id}"
os.makedirs(save_dir, exist_ok=True)

# 下载PDF
print("正在下载PDF...")
resp = requests.get(pdf_url, timeout=30)
resp.raise_for_status()

# 转换PDF为图片
print("正在转换PDF...")
images = convert_from_bytes(resp.content, fmt="jpg")

# 保存：页数_宽_高.jpg
for idx, img in enumerate(images, 1):
    w, h = img.size
    filename = f"{idx}_{w}_{h}.jpg"
    path = os.path.join(save_dir, filename)
    img.save(path, "JPEG")
    print(f"已保存: {path}")

print(f"✅ 转换完成！共 {len(images)} 页")
