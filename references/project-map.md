# 项目目录索引

本文件为 job-search-web skill 的目录导航。

## 目录结构

```
job-search-web/
├── SKILL.md                    # 主技能文件（入口）
├── references/                 # 参考文档（按需加载）
│   ├── project-map.md          # 本文件 - 目录索引
│   ├── search-urls.md          # 多平台搜索 URL 模板与城市代码
│   ├── search-checklist.md     # 多源检索检查清单
│   ├── standards.md            # 岗位信息整理标准
│   └── spec-alignment.md       # 字段与上游模型对齐说明
├── assets/                     # 输出模板与示例
│   ├── job-list-template.md    # 岗位列表 Markdown 模板（表格形式）
│   └── job-record.example.json # 岗位记录 JSON 示例
├── scripts/                    # 可执行脚本
│   └── dedupe_normalize.py     # 去重归一化脚本
└── code/                       # 参考源码（独立发布时随包携带）
    ├── README.md               # 源码说明
    └── config/
        └── application.yaml    # 配置片段
```

## 文件用途速查

| 需求 | 查阅文件 |
|------|----------|
| 构造各平台搜索 URL | [search-urls.md](search-urls.md) |
| 查询城市代码 | [search-urls.md](search-urls.md) |
| 了解可用的招聘网站源 | [search-checklist.md](search-checklist.md) |
| 规范化整理岗位信息 | [standards.md](standards.md) |
| 对齐上游 get_jobs 数据模型 | [spec-alignment.md](spec-alignment.md) |
| 输出表格格式岗位列表 | [../assets/job-list-template.md](../assets/job-list-template.md) |
| 输出 JSON 格式岗位记录 | [../assets/job-record.example.json](../assets/job-record.example.json) |
| 执行去重归一化 | [../scripts/dedupe_normalize.py](../scripts/dedupe_normalize.py) |
| 了解自动化工程结构 | [../code/README.md](../code/README.md) |
