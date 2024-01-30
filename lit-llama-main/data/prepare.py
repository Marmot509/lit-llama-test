import json

def process_lyrics_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as input_file, \
         open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            # 将每行文本转换成一个字典
            data = json.loads(line)
            # 获取歌词列表
            lyrics = data['lyric']
            # 使用逗号连接歌词，并在结尾添加句号
            processed_lyrics = ','.join(lyrics) + '。'
            # 将处理后的歌词写入到输出文件
            output_file.write(processed_lyrics + '\n')

# 调用函数处理文件
input_file_path = 'lyric_data_for_CL_no_id.jsonl'  # 将这里的路径替换为你的输入文件路径
output_file_path = 'lyrics.txt'  # 输出文件的路径
process_lyrics_file(input_file_path, output_file_path)
