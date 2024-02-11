import re

def remove_lines_with_digit(file_content):
    lines = file_content.split('\n')
    new_lines = []
    for line in lines:
        if not line.isdigit():
            new_lines.append(line)
    return '\n'.join(new_lines)

def remove_html_tags(file_content):
    cleanr = re.compile('<.*?>')
    return re.sub(cleanr, '', file_content)

def remove_lines_with_arrow(file_content):
    lines = file_content.split('\n')
    new_lines = []
    for line in lines:
        if '-->' not in line:
            new_lines.append(line)
    return '\n'.join(new_lines)

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='UTF-8') as file:
        content = file.read()

    content = remove_lines_with_digit(content)
    content = remove_html_tags(content)
    content = remove_lines_with_arrow(content)

    with open(output_file, 'w', encoding='UTF-8') as file:
        file.write(content)

# 设置输入和输出文件名
input_file = r'E:\library\taici\xxx.srt'
output_file = r'E:\library\taici\xxx.txt'

# 处理文件
process_file(input_file, output_file)