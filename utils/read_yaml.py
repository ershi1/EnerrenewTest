# coding: utf-8
import os
import yaml
from utils.logger import logger

pr_path = os.path.dirname(os.path.dirname(__file__))
extr_path = os.path.join(pr_path + '/data/extract.yaml')


def get_yaml_data(filepath):
    # 读取文件操作
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:  # file_object as f
            # 使用yaml方法获取数据
            result = yaml.load(f, Loader=yaml.FullLoader)
            return result
    except Exception as e:
        logger.exception(f"{e}---格式错误 请检查yaml文件编写规范哦。")
        print(f"{e}---格式错误 请检查yaml文件编写规范哦。")


def write_yaml(data):
    try:
        with open(extr_path, mode='a', encoding='utf-8') as f:
            yaml.dump(data, stream=f, allow_unicode=True)  # 加入unicode可以写入中文
    except Exception as e:
        print(e)


def clear_yaml():
    with open(extr_path, mode='w', encoding='utf-8') as f:
        f.truncate()
        print("data/extract.yaml文件的数据清除成功")


def replace_content(new_data):
    try:
        with open(extr_path, 'r') as file:  # 读取原文件的数据
            data = yaml.safe_load(file)
            for key, value in new_data.items():
                data[key] = value  # 存在同样的键则替换内容 不存在则写入

        # 写回YAML文件
        with open(extr_path, 'w') as file:  # 替换后的新数据写入文件
            yaml.dump(data, file, default_flow_style=False)

    except FileNotFoundError:
        print(f"Error: File {extr_path} not found.")
    except yaml.YAMLError as exc:
        print(exc)


# 1、判断header   2、判断是否提取参数 3、判断是否需要做关联
# 判断yaml用例中的关联参数值是否为空  为空则不需要做关联参数
# 如果不为空，则判断在extract文件中对应关键字参数是否为空，不为空就提取，为空就写人
# if __name__ == '__main__':
#     i = {"username":"admin-gov"}
#     try:
#         a = get_yaml_data(r'C:\Users\Administrator\.PyCharmCE2019.2\py_test\data\extract.yaml')['s']
#
#         #存在数据 就提取 传入json请求参数
#         i["s"] = a
#         print(i)
#
#     #不存在对应的键时，则会报异常 就进入了下面的流程
#     except:
#         #提取响应数据
#         get_data = get_text(re.json(), "'s'")
#         #把对应的数据通过键值对写入extract文件
#         write={"s": get_data}
#         write_yaml(write)
#         print(f"{write}写入成功")


if __name__ == '__main__':
    # a = get_yaml_data('../data/login_token.yaml')
    # print(a)
    b = get_yaml_data('../data/tf_project/FileUpload/test_upfile.yaml')['file']
    print(b)
    # print(pr_path)
