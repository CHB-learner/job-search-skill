# 参考源码说明

本目录包含上游 [get_jobs](https://github.com/loks666/get_jobs) 项目的参考源码摘录。

## 完整工程

要运行完整的自动化爬取工程，请克隆上游仓库：

```bash
git clone https://github.com/loks666/get_jobs.git
```

## 技术栈

- **后端**: Spring Boot
- **爬虫**: Playwright (支持动态页面)
- **数据存储**: MySQL / MongoDB
- **调度**: Spring Task / XXL-Job

## 支持站点

- BOSS直聘
- 猎聘
- 前程无忧 (51job)
- 智联招聘

## 目录结构

```
code/
├── README.md           # 本文件
└── config/
    └── application.yaml  # 配置片段示例
```

## 配置说明

详见 [config/application.yaml](config/application.yaml)

## 注意事项

1. **合规使用**: 遵守各站 robots.txt 和服务条款
2. **IP限制**: 不建议使用机房IP，容易触发反爬
3. **频率控制**: 合理设置请求间隔
4. **个人使用**: 禁止商业化滥用

## 相关链接

- 上游仓库: https://github.com/loks666/get_jobs
- 问题反馈: https://github.com/loks666/get_jobs/issues
