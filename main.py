# 读取 md 文件
with open('input.md', 'r', encoding='utf-8') as f:
    content = f.read()
# 将 ![[X]] 转换为 ![](X)
p1 = content.replace('![[', '![](')
new_content = p1.replace(']]', ')')
# 输出新的修改后的 md 文件
with open('output.md', 'w', encoding='utf-8') as f:
    f.write(new_content)