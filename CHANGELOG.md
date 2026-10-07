# CHANGELOG（software-testing）

只追加，不改写历史条目。

## 0.1.1 — resistance 约束补齐

- 新增 `resistance/resistance.md`（约束库索引，此前缺失致 `git工作流约束` 悬空）。
- 新增领域约束四条：`测试门禁/`（证据四件套＋五阻塞项＋三态结论）、
  `用例溯源/`（双向追溯＋孤儿用例禁止）、`委托边界/`（越界去向表＋伞形不重复）、
  `约束部分/`（红线区识别＋四段式＋只加严）。
- 新增 `审查约束/`：脚本判定优先、复审全项、禁止放宽参数。
- 新增 `scripts/scripts.md`、`references/references.md`、
  `references/编排判例/编排判例.md`（补 `逻辑链机制` 与 `update` 的悬空指向）。
- 修链接：`上下文压缩机制` 原指向本技能不存在的 `伞形不重复约束/`，
  改指 `委托边界`（内容未放宽，仅纠正指针）。
- 校验：`check_links.py` 悬空＝0、`check_len.py` 全 `.md` ≤50 行。

## 0.1.2 — branch 大纲与分支分析补齐
- 新增 `branch/流程/大纲.md`：13 步骤 → 68 子节点 → 进入条件／退出挂点，作为节点唯一清单
  （整体审查第 1 项「流程闭环」的比对基准）。
- 新增 `branch/流程/分支分析.md`：5 条分支线（A 创建主干／B 修改主干／C 失败回退／
  D 越界委派／E 门禁降级）的覆盖节点、进入退出条件、约束挂钩与节点跳转规则。
- `branch/流程/流程.md` 挂上大纲与分支分析链接（结构不变，仅新增指针）。
- `branch/branch.md` 索引与阅读顺序补「大纲／分支分析」两指针（既有链接一条未删）。
- 步骤与约束文件本轮未改动；既有 `resistance/` 条目只加严不放宽（见 `resistance/约束部分/`）。

## 0.1.3 — references 素材库落地（判例／模板／文献）
- 新增 `references/编排判例/ST-001-校验脚本参数面漂移.md`、
  `ST-002-有规则无条目.md`：两条均绑真实运行记录与提交号 `584cfdc`。
- 新增 `references/用例模板/`：`用例模板.md`（字段与编号口径）＋
  `夹具样例.md`（作用域与自建自毁判据），与 `branch/用例设计/` 字段定义一致。
- 新增 `references/上游文献/`：`上游文献.md` 索引 ＋ pytest 夹具与参数化、
  unittest 断言与用例组织、coverage 覆盖率证据三张摘录卡（PyPI 实核版本）。
- `references/references.md` 补「条目现状」表与「取用口径」（校验脚本一律带 `--root`）。
- 接线：`branch/流程/流程.md` 挂素材入口；`branch/知识库构建/` 第 3 步加「规则与条目
  同轮落地」严判、第 4 步要求更新条目现状表；`branch/经验查询/` 第 1、2 步改指实际目录，
  并加「命中为空须显式记录」判据（均只加严，未放宽任何约束）。
- `dependence/deps.json` 登记 9 条：pytest 9.1.1(MIT)、coverage.py 7.16.2(Apache-2.0)、
  unittest(PSF-2.0)，以及 general-programming / python-expert / cpp-expert /
  webapp-testing / packaging-and-release / git-remote-management（`local://`）。
- 校验：`check_links`＝悬空 0、`check_len`＝全部 .md ≤50 行、`lint_deps` 通过、
  `deps_check` 本地技能全可达。红线区既有条目一字未删。
