# 字段与上游模型对齐说明

本说明用于对齐 skill 输出与上游 [get_jobs](https://github.com/loks666/get_jobs) 项目的数据模型。

## 上游数据模型（参考）

基于 get_jobs 项目的 Java 实体类，主要字段：

```java
// 简化示意，非完整代码
public class JobInfo {
    private String id;              // 唯一标识
    private String positionName;    // 职位名称
    private String company;         // 公司名称
    private String location;        // 工作地点
    private String salary;          // 薪资范围
    private String workYear;        // 工作年限
    private String education;       // 学历要求
    private String jobDetail;       // 职位描述
    private String companySize;     // 公司规模
    private String industry;        // 行业领域
    private String url;             // 来源URL
    private String source;          // 来源站点
    private Date publishTime;       // 发布时间
    private Date crawlTime;         // 抓取时间
}
```

## 字段映射

| skill 字段 | 上游字段 | 说明 |
|------------|----------|------|
| 职位名称 | positionName | 直接对应 |
| 公司名称 | company | 直接对应 |
| 工作地点 | location | 直接对应 |
| 薪资范围 | salary | 直接对应 |
| 工作年限 | workYear | 直接对应 |
| 学历要求 | education | 直接对应 |
| 职位描述 | jobDetail | 直接对应 |
| 公司规模 | companySize | 直接对应 |
| 行业领域 | industry | 直接对应 |
| 来源URL | url | 直接对应 |
| 来源站点 | source | 需从 URL 提取域名 |
| 发布时间 | publishTime | 需解析原始描述 |
| 技能标签 | - | skill 扩展字段，从 JD 提取 |

## 扩展字段

skill 在上游模型基础上扩展：

| 扩展字段 | 说明 | 来源 |
|----------|------|------|
| 技能标签 | 从 JD 提取的关键技能 | NLP/规则提取 |
| 薪资下限 | 薪资范围解析 | 正则提取 |
| 薪资上限 | 薪资范围解析 | 正则提取 |
| 薪资月数 | 年薪月数（如16薪） | 正则提取 |

## 数据流转

```
用户检索 → skill 整理 → JSON 输出 → 可导入 get_jobs 分析
```

## 兼容性

- JSON 输出格式与上游模型兼容
- 可直接用于 get_jobs 的数据导入
- 扩展字段不影响上游字段解析
