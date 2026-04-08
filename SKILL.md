---
name: job-search-web
description: "指导用户与代理在多源网站（招聘站、聚合页、企业官网、社区与远程岗位列表）系统性检索与汇总岗位；含去重、筛选、合规边界。本地落地自动化可参考仓库 get_jobs（Boss/猎聘/51job/智联、Playwright、Spring Boot）。在用户要「找工作、搜岗位、全网职位、聚合招聘信息、用 get_jobs」时使用本 skill。触发词：找工作、搜岗位、职位搜索、招聘信息聚合。"
---

# 全网找工作（Job Search Web）

## 使用边界（硬约束）

- **合规**：遵守各站服务条款与 robots；不协助破解登录、绕过反爬、批量爬取受保护页面；**不鼓励**用机房/服务器 IP 访问招聘站（上游 get_jobs README 亦提示）。
- **用途**：辅助用户发现与整理岗位信息；上游 **get_jobs** 为开源参考，**禁止商业化与滥用**（见上游协议与说明）。
- **本包范围**：`code/` 为参考源码摘录；**可运行完整工程**须克隆 [get_jobs](https://github.com/loks666/get_jobs)。单独发布本 skill 时，请**整包复制**根目录下全部内容（含 `SKILL.md`、`references/`、`assets/`、`scripts/`、`code/`），不依赖本机其它路径。

## 执行步骤（主路径，须先完成）

1. **澄清需求**：岗位类型、城市/远程、薪资、全职或实习、需排除的行业与公司类型。
2. **多源检索**：依次访问 BOSS直聘、前程无忧、猎聘、智联招聘四大平台；URL 模板与参数见 [references/search-urls.md](references/search-urls.md)。
3. **汇总与去重**：优先稳定 URL；否则用「公司名 + 职位名 + 地点」归一；可用 [scripts/dedupe_normalize.py](scripts/dedupe_normalize.py) 生成归一化键。整理标准见 [references/standards.md](references/standards.md)。
4. **输出**：使用 [assets/job-list-template.md](assets/job-list-template.md) 以表格形式输出，每行一条岗位，附原始链接。
5. **自动化落地**：查阅 `code/` 与 [code/README.md](code/README.md)；端口与配置片段见 `code/config/application.yaml`。

## 多平台检索流程

### 平台优先级

| 优先级 | 平台 | 特点 | 访问方式 |
|--------|------|------|----------|
| 1 | BOSS直聘 | 直聊模式，响应快，岗位新 | 需登录，反爬严格 |
| 2 | 猎聘 | 中高端岗位多，猎头资源 | 部分需登录 |
| 3 | 前程无忧 | 传统招聘站，岗位全 | 界面较老，信息全 |
| 4 | 智联招聘 | 传统招聘站，覆盖广 | 部分信息需登录 |

### 检索策略

1. **并行检索**：同时打开多个平台标签页，提高效率
2. **关键词统一**：使用相同的关键词组合（岗位名 + 城市 + 技能）
3. **时间过滤**：优先近 7 天发布的岗位
4. **交叉验证**：同一岗位在多站出现时，优先企业官网信息

### URL 构造指南

详见 [references/search-urls.md](references/search-urls.md)，包含：
- 各平台搜索 URL 模板
- 城市代码对照表
- 薪资/经验筛选参数

## 按需加载（勿一次性读完）

| 类型 | 位置 | 说明 |
|------|------|------|
| 搜索 URL 模板与城市代码 | [references/search-urls.md](references/search-urls.md) | 多平台 URL 构造指南 |
| 长检查清单、规范 | [references/](references/project-map.md) | 内容较长，仅在需要时读取 |
| 固定版式、示例占位 | [assets/](assets/job-list-template.md) | 模板与示例输出，可反复套用 |
| 可重复执行的脚本 | [scripts/](scripts/dedupe_normalize.py) | 归一化键等，直接调用 |
| 参考源码与配置 | [code/](code/README.md) | Java 模型与 YAML 节选，独立发布随包携带 |

目录索引：[references/project-map.md](references/project-map.md)。
