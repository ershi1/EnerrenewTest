# 获取响应参数(可以提取多个根据yaml文件的 response_extraction来判断)，自定义键然后写入文件/data/extract.yaml 文件
def get_resp(response, extract_key, apiname):
    """
    :param response:     请求的响应数据
    :param extract_key:  需要写入yaml文件的自定义关键字加值  key：value
    :return:01
    """

    if extract_key:
        try:
            for i in extract_key:
                if "rex" in i.keys():

                    yaml_result = i.get("rex")[0]  # jsonpath提取器定位方法

                    # actual_result = jsonpath.jsonpath(response.json(),f'$..{yaml_result}')#去掉 $..
                    # 是考虑返回的json数据如果存在两个一样的id
                    extract_value = jsonpath.jsonpath(response.json(),
                                                      yaml_result)  # jsonpath提取的值  取到的值返回在列表里 如 [200]

                    input_key = i.get("rex")[1]  # 自定义的键
                    # print(input_key)
                    new_dict = {input_key: extract_value[0]}
                    # write_yaml(new_dict)  # 写入yaml文件
                    replace_content(new_dict)  # 此方式可以替换相同的字典

                    logger.info(
                        f"正在注入变量>>>>>> 成功提取响应数据，并自定义关键字{new_dict}>>>>写入extract.yaml关联文件")

                elif "re" in i.keys():  # 正则表达式
                    yaml_result = i.get("re")[0]
                    ex_value = re.search(yaml_result, response.text())
                    input_key = i.get("rex")[1]  # 自定义的键
                    # print(input_key)
                    new_dict = {input_key: ex_value}
                    # write_yaml(new_dict)  # 写入yaml文件
                    replace_content(new_dict)  # 此方式可以替换相同的字典
                    logger.info(
                        f"正在注入变量>>>>>> 成功提取响应数据，并自定义关键字{new_dict}>>>>写入extract.yaml关联文件")
                    pass

        except Exception as e:
            # logger.info(f"jsonpath （响应数据）提取失败__请检查{extract_key}写法是否正确。异常信息为：{e}，接口返回值为：{response.json()}")
            logger.exception(
                f"jsonpath （响应数据）提取失败__请检查 {yaml_result} 写法是否正确。异常信息为：{e}，接口返回值文本信息为：{response.content.decode()}")
            raise AssertionError(
                f"用例名称：{apiname}-->（接口响应数据）提取失败_请检查 {yaml_result} 写法是否正确。异常信息为：{e}，接口返回值文本信息为：{response.content.decode()}")  # 抛出异常后  程序终止 后面的程序不在执行
            # print(f"jsonpath提取器提取失败请检查写法是否正确。异常信息为：{e}")
