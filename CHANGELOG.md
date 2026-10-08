# CHANGELOG（software-testing）
只追加，不改写历史条目。历史条目 0.1.1–0.1.3 **逐字迁出**至
[CHANGELOG-0.1.1-0.1.3.md](CHANGELOG-0.1.1-0.1.3.md)（仅换承载文件，正文一字未改），
迁出仅因 `check_len.py` 每 `.md` ≤50 行红线（换承载不改正文，动作口径见
[ST-003](references/编排判例/ST-003-根文档与清单一致性.md)）；迁出与新增同轮落地（[ST-002](references/编排判例/ST-002-有规则无条目.md)口径）。
## 0.1.5 — 依赖清单补至十三余条 + 属性测试文献卡
- `dependence/deps.json` 由 9 条增至 13 条：新增 pytest-cov 7.1.0(MIT)、
  hypothesis 6.168.5(MPL-2.0)、mutmut 3.8.0(BSD-3-Clause)、nox 2026.8.17(Apache-2.0)，
  版本号与许可表达式经 PyPI `license_expression` 实时核验（2026-10-08）。
- 新增摘录卡 `references/上游文献/hypothesis-属性测试与收缩.md`（收缩＋种子＝可复现证据口径），
  索引同步 `上游文献.md` 与 `references.md`。
- `branch/用例设计/` 增第 6 项「属性用例」，指针指向新卡（规则与条目同轮落地，
  口径见 [ST-002](references/编排判例/ST-002-有规则无条目.md)）。
## 0.1.4 — 根文档补齐（README／CONTRIBUTORS）＋根文档一致性判例
- 新增 `README.md`（34 行）：定位、目录结构表、快速上手（四条校验命令＋续跑入口）、
  门禁口径（证据四件套／禁修绿）、边界与许可指针。
- 新增 `CONTRIBUTORS.md`（28 行）：维护者／贡献者（`Skill_Generator`、
  `general-software-dev` 委派、工具自办步、被派发技能去向）＋贡献方式五条＋约定许可。
- 实测更正：`scripts/` 12 个 `.py` 与 `scripts/scripts.md` 12 行清单**一一对齐**，
  本轮未增删脚本（上一轮曾误记「待补 test_runner／coverage_gate」，此处以实盘为准）。
- 新增判例 `references/编排判例/ST-003-根文档与清单一致性.md`：把「根文档缺失／
  清单与实存文件漂移」固化为可复跑判据（README＋CONTRIBUTORS 必存在，
  `scripts/*.py` 全数出现在 `scripts.md`），证据＝`129ffa3` 时目录实盘。
- 接线（只加严）：`branch/收尾/收尾.md` 第 4 步「提示词与骨架同步」扩为
  根文档一致性（SKILL／README／CONTRIBUTORS／CHANGELOG 四处口径不得互斥）；
  `branch/整体审查/整体审查.md` 第 4 项「目录规范」加严为须核根文档存在＋
  脚本清单与实存文件对得上；`references/references.md` 条目现状表加 ST-003；
  `scripts/scripts.md` 加「根文档一致性」小节；`SKILL.md` 末段加 `README.md`／
  `CONTRIBUTORS.md` 指针，`version` 随本轮条目升 0.1.4（只加指针与版本号，
  工作原则与红线摘要未放宽）。
- 校验（本轮真实运行）：`check_links`＝悬空 0、`check_len`＝全部 .md ≤50 行、
  `lint_deps` 通过、`deps_check` 本地技能全可达。红线区既有条目一字未删未放宽。
- git：`feature/root-docs` 建分支与提交**受阻**（git 写须当轮 danger 授权，
  本轮未获），0.1.4 改动落 `dev` 工作树未入库——按 git工作流约束如实记受阻并跳过。
