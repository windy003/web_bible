import os
import re

# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

for filename in os.listdir(script_dir):
    if filename.startswith("第"):
        # 提取章节数字
        chapter_number = re.search(r'第(\d+)章', filename)
        if chapter_number:
            new_name = chapter_number.group(1)
            # 保留原文件扩展名(如果有)
            if "." in filename:
                extension = filename.split(".")[-1]
                new_name = f"{new_name}.{extension}"
            # 重命名文件
            try:
                os.rename(
                    os.path.join(script_dir, filename),
                    os.path.join(script_dir, new_name)
                )
                print(f"成功重命名: {filename} -> {new_name}")
            except Exception as e:
                print(f"无法重命名 {filename}: {str(e)}")

print("重命名完成!")
