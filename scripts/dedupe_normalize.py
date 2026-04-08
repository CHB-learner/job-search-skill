#!/usr/bin/env python3
"""
岗位去重归一化脚本

功能：
1. 生成归一化键（公司名 + 职位名 + 地点）
2. 基于归一化键去重
3. 输出去重后的岗位列表

使用方法：
    python dedupe_normalize.py input.json output.json
    python dedupe_normalize.py --stdin < input.json > output.json
"""

import json
import re
import sys
from typing import Dict, List, Any


def normalize_company(name: str) -> str:
    """归一化公司名称"""
    if not name:
        return ""
    
    # 去除常见后缀
    suffixes = [
        "有限公司", "有限责任公司", "股份有限公司",
        "科技有限公司", "网络科技有限公司", "信息技术有限公司",
        "软件有限公司", "技术服务有限公司", "集团",
        "（中国）", "(中国)", "（北京）", "(北京)"
    ]
    
    result = name.strip()
    for suffix in suffixes:
        result = result.replace(suffix, "")
    
    # 去除多余空格
    result = re.sub(r'\s+', '', result)
    
    return result.lower()


def normalize_position(name: str) -> str:
    """归一化职位名称"""
    if not name:
        return ""
    
    # 去除修饰词
    modifiers = [
        "急聘", "高薪", "诚聘", "急招", "热招", "火热招聘",
        "【", "】", "（", "）", "(", ")"
    ]
    
    result = name.strip()
    for mod in modifiers:
        result = result.replace(mod, "")
    
    # 去除多余空格
    result = re.sub(r'\s+', '', result)
    
    return result.lower()


def normalize_location(location: str) -> str:
    """归一化地点（城市级别）"""
    if not location:
        return ""
    
    # 提取城市名
    city_patterns = [
        r'^([^省市县区]+?[省市])',
        r'^([^市]+?市)',
        r'^北京',
        r'^上海',
        r'^广州',
        r'^深圳',
        r'^杭州',
        r'^成都',
        r'^南京',
        r'^武汉',
        r'^西安',
    ]
    
    result = location.strip()
    
    for pattern in city_patterns:
        match = re.search(pattern, result)
        if match:
            result = match.group(0)
            break
    
    # 去除区县信息
    result = re.sub(r'[区县].*$', '', result)
    
    return result.lower()


def generate_normalize_key(job: Dict[str, Any]) -> str:
    """生成归一化键"""
    company = normalize_company(job.get("公司名称", job.get("company", "")))
    position = normalize_position(job.get("职位名称", job.get("positionName", "")))
    location = normalize_location(job.get("工作地点", job.get("location", "")))
    
    return f"{company}|{position}|{location}"


def dedupe_jobs(jobs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """去重岗位列表"""
    seen = {}
    result = []
    
    for job in jobs:
        key = generate_normalize_key(job)
        
        if key not in seen:
            seen[key] = job
            # 添加归一化键到输出
            job["归一化键"] = key
            result.append(job)
        else:
            # 保留信息更完整的记录
            existing = seen[key]
            if len(str(job)) > len(str(existing)):
                result.remove(existing)
                job["归一化键"] = key
                result.append(job)
                seen[key] = job
    
    return result


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python dedupe_normalize.py input.json [output.json]")
        print("      python dedupe_normalize.py --stdin < input.json > output.json")
        sys.exit(1)
    
    # 读取输入
    if sys.argv[1] == "--stdin":
        data = json.load(sys.stdin)
    else:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            data = json.load(f)
    
    # 获取岗位列表
    if isinstance(data, list):
        jobs = data
    elif isinstance(data, dict):
        jobs = data.get("岗位列表", data.get("jobs", []))
    else:
        print("错误: 输入格式不正确")
        sys.exit(1)
    
    # 去重
    deduped = dedupe_jobs(jobs)
    
    # 构建输出
    if isinstance(data, dict):
        output = data.copy()
        output["岗位列表"] = deduped
        if "统计信息" in output:
            output["统计信息"]["去重后数量"] = len(deduped)
    else:
        output = deduped
    
    # 写入输出
    if len(sys.argv) >= 3:
        with open(sys.argv[2], 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        print(f"去重完成: {len(jobs)} -> {len(deduped)} 条记录")
    else:
        print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
