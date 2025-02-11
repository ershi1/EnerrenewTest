graph TD
    A[测试用例] --> B[调用Service层]
    B --> C{是否需预处理}
    C -->|是| D[中间件处理]
    C -->|否| E[调用API Client]
    E --> F[发送实际请求]
    F --> G[获取响应]
    G --> H[断言验证]
    H --> I[生成测试报告]
          