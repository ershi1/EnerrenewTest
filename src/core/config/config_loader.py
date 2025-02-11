import yaml
import os
from pathlib import Path
from typing import Dict

_ENV = os.getenv("ENVIRONMENT", "dev")  # 通过环境变量切换配置

def load_config() -> Dict:
    config_path = Path(__file__).parent / "environments" / f"{_ENV}.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

import os
from configparser import ConfigParser


class Docof():
    def __init__(self, file_name='config.yaml'):
        file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r'\conf\\' + file_name
        self.cp = ConfigParser()
        self.cp.read(file_path, encoding='utf8')

    def get_all_sections(self):
        # 获取所有节点 列表返回
        return self.cp.sections()
        # 获取某个节点里面option对应的值

    def get_value_from_option(self, section, option):
        """
        :param section: 节点名（http）
        :param option:节点下面的选项（url）
        :return:
        """
        return self.cp.get(section, option)

    def get_option(self, option):
        """
        获取节点下的option
        :param option:
        :return:
        """
        return self.cp.options(option)

    # 获取指定分组的键值对
    def get_items(self, section):
        return self.cp.items(section)

    cof = read_config.Docof()
    # test_*执行文件
    sys = cof.get_value_from_option("environment", "sys_name")  # 本次执行的项目名称

    # BusinessFlow_convert.py
    Excel_yaml = cof.get_value_from_option("Excel_yaml", "tests")  # 根据配置文件来整合 execl或者yaml 用例

    # send_port.py
    send_email = cof.get_value_from_option('send_email', 'send_or_not')  # 读取配置文件 判断是否需要发送报告

    # util
    exect = cof.get_value_from_option("environment", "execute")
    ip = cof.get_value_from_option("environment", exect)

if __name__ == '__main__':
    dc = Docof()
    # 执行环境的url读取
    exect = dc.get_value_from_option("environment", "execute")
    url = dc.get_value_from_option("environment", exect)
    print(url)