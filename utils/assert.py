
# jsonpath 断言
def assert_response(response, validate, apiname):
    """
    :param response: 接口响应数据
    :param validate: 提取响应数据进行断言
    :return:
    """
    # validate等于[{'eq': ['$.code', 200]}, {'eq': ['$.message', '请求成功']}]
    # logger.info(f"接口预期结果 {validate}")
    # try:
    logger.info(f"接口返回文本信息<<<<<<<{response.content.decode()}")  # 就算返回的不是json数据 也能打印出当前源码内容
    logger.info("开始断言--->>>>")
    for i in validate:

        if "eq" in i.keys():
            try:
                yaml_result = i.get("eq")[0]
                actual_result = jsonpath.jsonpath(response.json(), yaml_result)  # jsonpath提取的值  取到的值在列表里 如 [200]
                expect_result = i.get("eq")[1]  # yaml文件中 写的期望值
            except Exception as e:
                logger.exception(f"error: {e}")
            try:

                assert actual_result[0] == expect_result
                logger.info(f"---->>>>{apiname}接口: {expect_result} 等值断言成功")
                # 这里不能写return 不然只会断言1个数据  就不在循环
            except AssertionError:
                logger.exception(
                    f"(等值断言失败)-->>接口期望结果【{expect_result}】 ≠ 接口实际结果【{actual_result[0]}】")  # 打印到日志里面
                raise AssertionError(
                    f"接口标题：{apiname}(等值断言失败)-->>接口期望结果【{expect_result}】 ≠ 接口实际结果【{actual_result[0]}】")  # 抛出异常 否则assert断言会一直成功

        # 在使用Python3做自动化测试过程中可能会遇到,assert函数不加try  except，就可以正常在报告里体现用例不通过，
        # 加上变成通过。这是因为在使用try except 时,捕获了assert函数产生的AssertionError异常,导致异常没有上抛,这时只需要在后面加上 raise 就可以再次把它抛出。

        elif "contain" in i.keys():  # 文本包含断言
            result = response.text  # jsonpath提取的文本
            expect = i.get("contain")[0]  # yaml文件中 写的期望值

            try:
                assert expect in result  # 文本包含断言
                logger.info(f"---->>>>{apiname}接口: {expect_result} 文本包含断言成功")

            except AssertionError:
                logger.exception(
                    f"(等值断言失败)-->>接口期望结果【{expect_result}】 ≠ 接口实际结果【{actual_result[0]}】")
                # 上行扑捉了异常， 下行raise不抛异常的话   aller报告上面 会默认执行成功  allure报告认AssertionError异常
                raise AssertionError(
                    f"接口标题：{apiname}(文本包含断言失败)-->>接口期望结果【{expect}】 ≠ 接口实际结果【{result}】 ")

        elif "regex_match" in i.keys():  # 正则表达式 断言
            pass
            # 要对一个查询类接口的返回数据进行验证，我们可以采用编写SQL，到数据查询结果，然后将数据库结果与接口返回结果进行核对检查，这样就能比较准确的验证接口返回数据的正确性。
        elif "db" in i.keys():  # 数据库断言  - db: ["SELECT * FROM system_book WHERE `name`='python数据构造'",1]
            try:
                sql = i.get("db")[0]  # 提取sql语句
                d = DB()  # 实例化
                le = d.query(sql)  # 实际查出结果数量
                resu = i.get("db")[1]  # 期望结果查询出来的数据有几条和期望结果做对比
                assert len(le) == resu
                logger.info(f"---->>>>{apiname}接口: {expect_result} 数据库断言成功")
            except AssertionError as e:
                logger.exception(f"db断言失败哦 请检查{sql}")
                raise AssertionError(f"db断言失败哦 请检查{sql}")

    logger.info(f"接口测试结果>>>>>>   {apiname}  ---->>>>>>测试通过 <<<<<<")
    logger.info(f"==================================接口t用例执行结束: {apiname}==================================")