def remove_words(file_a_path, file_b_path, file_c_path):
    try:
        # 读取文件B中的单词，存储在集合中以便快速查找
        with open(file_b_path, 'r', encoding='utf-8') as file_b:
            words_in_b = set(file_b.read().splitlines())

        # 读取文件A，并检查每个单词是否在文件B的集合中
        with open(file_a_path, 'r', encoding='utf-8') as file_a:
            words_in_a = file_a.read().splitlines()

        # 准备写入文件C的单词列表
        words_to_write = [word for word in words_in_a if word not in words_in_b]

        # 写入文件C
        with open(file_c_path, 'w', encoding='utf-8') as file_c:
            for word in words_to_write:
                file_c.write(word + '\n')

        print("处理完成，结果已保存到文件C")
    except Exception as e:
        print(f"发生错误：{e}")

# 主函数，用于获取文件路径并调用处理函数
def main():
    file_a = input("请输入文件A的路径: ")
    file_b = input("请输入文件B的路径: ")
    file_c = input("请输入输出文件C的路径: ")
    remove_words(file_a, file_b, file_c)

if __name__ == "__main__":
    main()