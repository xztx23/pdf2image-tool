# PDF 转图片工具（GitHub Actions 版）

本仓库通过 GitHub Actions 实现 PDF 在线转图片，无需本地环境，只需传入 PDF 链接和学生学号即可自动完成转换。

## 触发方式
在仓库主页 → Actions → 选择 `PDF to Images` 工作流 → 点击 `Run workflow`：
1. 输入 `pdf_url`：PDF 文件的直接下载链接
2. 输入 `student_id`：学生学号（用于创建分类文件夹）
3. 点击 `Run workflow` 即可

## 输出结果
转换后的图片会自动保存在仓库的 `images/学生学号/` 目录下，命名规则为：
`{页码}_{宽度}_{高度}.jpg`

例如：`images/2025001001/1_1700_2200.jpg`
