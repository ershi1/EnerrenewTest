# -*- coding: utf-8 -*-
# @Time    : 2023/5/26 0026 15:39
# @Author  : zcj
# @File    : single_convert.py
# @Software : PyCharm
from common.util import single_path, filename_all

from common.read_yaml import get_yaml_data

# ta = get_yaml_data(single_path + f'/test_single.yaml')["one"]  # 读取节点下全部数据

data1 = [{'id': 1, 'request': {'url': 'http://192.167.6.185:8090/dah-park-api/unit-document/page', 'method': 'GET'},
          'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate',
                      'Accept-Language': 'zh-CN,zh;q=0.9'},
          'relation': None,
          'parametrize': [{'title': '错误的入参', 'json': {'pageNum': 1, 'pageSize': 20}, 'ex': [{'eq': ['$.code', 200]}]},
                          {'title': '错误的数据', 'json': {'pageNum': 1, 'pageSize': 20}, 'ex': [{'eq': ['$.code', 200]}]},
                          {'title': None, 'json': {'pageNum': 1, 'pageSize': 20}, 'ex': [{'eq': ['$.code', 200]}]}]}]


def single_data_convert(data):
    d = []
    for a in data:
        # 有几个单接口用例  就循环读取节点下的 参数化的数据
        info = a["parametrize"]
        #
        for i in info:
            """
             有几个迭代对象(测试用例)，就循环几次，每次向用例字典 添加公共（url、method、headers、relation）元素  
             {'title': '错误的入参', 'json': {'pageNum': 1, 'pageSize': 20}, 'expected': [{'eq': ['$.code', 200]}], 
             'request': {'url': 'http://192.167.6.185:8090/dah-park-api/unit-document/page', 'method': 'GET'}, 
             'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}, 'relation': None}
            """
            i["request"] = a["request"]
            i["headers"] = a["headers"]
            i["relation"] = a["relation"]
            i["describe"] = a["describe"]  # 字典不存在在 创建 添加到大列表中
            i["response_extraction"] = a["response_extraction"]
            d.append(i)
    return d
"""
d=[{'title': '错误的入参', 'json': {'pageNum': 1, 'pageSize': 20}, 'expected': [{'eq': ['$.code', 200]}], 'request': {'url': '/dah-park-api/unit-document/page', 'method': 'GET'}, 'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}, 'relation': None, 'module_name': '一企一档模块'}, 
{'title': '错误的数据', 'json': {'pageNum': 1, 'pageSize': 20}, 'expected': [{'eq': ['$.code', 200]}], 'request': {'url': '/dah-park-api/unit-document/page', 'method': 'GET'}, 'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}, 'relation': None, 'module_name': '一企一档模块'},
{'title': '异常数据类型', 'json': {'pageNum': 1, 'pageSize': 20}, 'expected': [{'eq': ['$.code', 200]}], 'request': {'url': '/dah-park-api/unit-document/page', 'method': 'GET'}, 'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}, 'relation': None, 'module_name': '一企一档模块'}, 
{'title': '代入关键字参数', 'json': {'pageNum': 1, 'pageSize': 20}, 'expected': [{'eq': ['$.code', 200]}], 'request': {'url': '/dah-park-api/unit-document/page', 'method': 'GET'}, 'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}, 'relation': None, 'module_name': '一企一档模块'}, 
{'title': '参数为空', 'json': {'pageNum': 1, 'pageSize': 20}, 'expected': [{'eq': ['$.code', 200]}], 'request': {'url': '/dah-park-api/unit-document/page', 'method': 'GET'}, 'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}, 'relation': None, 'module_name': '一企一档模块'}, 
{'title': '电话加密', 'json': {'pageNum': 1, 'pageSize': 20}, 'expected': [{'eq': ['$.code', 200]}], 'request': {'url': '/dah-park-api/unit-document/page', 'method': 'GET'}, 'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}, 'relation': None, 'module_name': '一企一档模块'}, 
{'title': '错误的入参2', 'json': {'pageNum': 1, 'pageSize': 20}, 'expected': [{'eq': ['$.code', 200]}], 'request': {'url': '/dah-park-api/hazardous-chemicals/page?', 'method': 'GET'}, 'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}, 'relation': None, 'module_name': '应急管理模块'}, 
{'title': '错误的数据2', 'json': {'pageNum': 1, 'pageSize': 20}, 'expected': [{'eq': ['$.code', 200]}], 'request': {'url': '/dah-park-api/hazardous-chemicals/page?', 'method': 'GET'}, 'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}, 'relation': None, 'module_name': '应急管理模块'}, 
{'title': '异常数据类型2', 'json': {'pageNum': 1, 'pageSize': 20}, 'expected': [{'eq': ['$.code', 200]}], 'request': {'url': '/dah-park-api/hazardous-chemicals/page?', 'method': 'GET'}, 'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}, 'relation': None, 'module_name': '应急管理模块'}, 
{'title': '代入关键字参数2', 'json': {'pageNum': 1, 'pageSize': 20}, 'expected': [{'eq': ['$.code', 200]}], 'request': {'url': '/dah-park-api/hazardous-chemicals/page?', 'method': 'GET'}, 'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}, 'relation': None, 'module_name': '应急管理模块'}, 
{'title': '参数为空2', 'json': {'pageNum': 1, 'pageSize': 20}, 'expected': [{'eq': ['$.code', 200]}], 'request': {'url': '/dah-park-api/hazardous-chemicals/page?', 'method': 'GET'}, 'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}, 'relation': None, 'module_name': '应急管理模块'}, 
{'title': '电话加密2', 'json': {'pageNum': 1, 'pageSize': 20}, 'expected': [{'eq': ['$.code', 200]}], 'request': {'url': '/dah-park-api/hazardous-chemicals/page?', 'method': 'GET'}, 'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}, 'relation': None, 'module_name': '应急管理模块'}]
"""


# print(single_data_convert(ta))
# 将指定目录下的所有文件 的用例 添加在一个列表中
def allcase_single():
    cases = []
    num = filename_all(single_path)
    if num:
        for filename in num:
            ta = get_yaml_data(single_path + f'/{filename}')["one"]  # 读取节点下全部数据
            case = single_data_convert(ta)
            cases.extend(case)

        return cases
    else:

        print("单接口目录下，不存在用例文件")

if __name__ == '__main__':
    print(len(allcase_single()))