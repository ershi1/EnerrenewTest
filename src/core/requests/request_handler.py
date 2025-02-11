import json

class ResponseHandler:
    @staticmethod
    def validate_response(response: dict, schema: dict) -> bool:
        """校验响应数据结构"""
        # 示例: 使用 JSON Schema 校验
        from jsonschema import validate
        try:
            validate(instance=response, schema=schema)
            return True
        except Exception as e:
            raise ValueError(f"响应校验失败: {str(e)}")

    @staticmethod
    def extract_field(response: dict, field_path: str):
        """从嵌套字典中提取字段"""
        keys = field_path.split(".")
        value = response
        for key in keys:
            value = value.get(key)
            if value is None:
                break
        return value