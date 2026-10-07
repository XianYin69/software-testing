---
name: software-testing
version: 0.1.3
description: >
  软件测试技能：测试策略/用例设计/自动化执行/失败分诊/质量门禁，
  语言专项派 general-programming·python-expert·cpp-expert，
  Web E2E 派 webapp-testing；本技能只管测试链路与放行判据。
license: MIT
metadata:
  category: development
---

# software-testing

使用 `software-testing` skill 来完成用户请求。

## 工作原则

1. **按流程执行**：不跳步、不静默越权；决策节点留逻辑链。
2. **风险驱动**：测试深度按变更面与失效代价定，不按习惯铺全量。
3. **用例可追溯**：用例绑需求/缺陷号，可复跑、可归因、可沉淀。
4. **失败先分诊**：真缺陷／用例脆弱／环境抖动三分后再定责。
5. **门禁即证据**：放行只认真实运行记录，无证据不放行。
6. **不重复他人**：写实现派语言专家，Web E2E 派 webapp-testing。
7. **惩罚熔断**：同一重试达 10 次即熔断；tmp 释放后删除。

## 执行路径

**创建路径**：[初始化](branch/初始化/初始化.md)→[需求确认](branch/需求确认/需求确认.md)→
[经验查询](branch/经验查询/经验查询.md)→[测试策略](branch/测试策略/测试策略.md)→
[用例设计](branch/用例设计/用例设计.md)→[自动化执行](branch/自动化执行/自动化执行.md)→
[失败分诊](branch/失败分诊/失败分诊.md)→[质量门禁](branch/质量门禁/质量门禁.md)→
[知识库构建](branch/知识库构建/知识库构建.md)→[约束编写](branch/约束编写/约束编写.md)→
[整体审查](branch/整体审查/整体审查.md)→[收尾](branch/收尾/收尾.md)→**完成**
**修改路径**：[初始化](branch/初始化/初始化.md)→[修改流程](branch/修改流程/修改流程.md)→**完成**

## 红线摘要

- 无策略不写用例、无用例不跑自动化、未过门禁不放行
  （[测试门禁](resistance/测试门禁/测试门禁.md)）。
- 失败不得靠放宽断言／跳过用例／调大超时「修绿」；flaky 须留证据与去向。
- 每条用例必绑 trace，无 trace 即孤儿不入库（[用例溯源](resistance/用例溯源/用例溯源.md)）。
- 越界不自己做：实现／Web E2E／发布／远程协作各有去向
  （[委托边界](resistance/委托边界/委托边界.md)）。
- 悬空链接＝0；所有 `.md` ≤50 行；脚本英文名；缓存不入 skill 目录。

总览与步骤表：[branch/流程/](branch/流程/流程.md)；分支索引：[branch/](branch/branch.md)；
约束库总索引：[resistance/](resistance/resistance.md)。
