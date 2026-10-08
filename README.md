# software-testing
软件测试技能：**测试策略 → 用例设计 → 自动化执行 → 失败分诊 → 质量门禁** 的链路与放行判据。
实现派 `general-programming`／`python-expert`／`cpp-expert`，Web E2E 派 `webapp-testing`，
发布动作派 `packaging-and-release`（去向表见
[委托边界](resistance/委托边界/委托边界.md)）。
## 结构
- [SKILL.md](SKILL.md)：入口（YAML frontmatter）＋工作原则＋红线摘要。
- [agent/](agent/instructions.md)：四格式提示词（CLAUDE.md／.cursorrules／instructions.md／agent_prompt.md）。
- [branch/](branch/branch.md)：分支库（创建 12 步＋修改 1 步）；节点唯一清单见
  [大纲](branch/流程/大纲.md)，分支线跳转规则见 [分支分析](branch/流程/分支分析.md)。
- [scripts/](scripts/scripts.md)：13 个英文命名脚本；写盘类默认预览，`--yes` 才落地。
- [references/](references/references.md)：素材库（编排判例／用例模板／上游文献）。
- [resistance/](resistance/resistance.md)：约束库＋五机制（逻辑链／过程链／惩罚／压缩／回收）。
- [dependence/](dependence/dependence.md)：依赖清单＋ [deps.json](dependence/deps.json)（每条附 `source_url`）。
- [planned_tasks/](planned_tasks/README.md)：计划任务声明（到期由 SMS 调度器执行）。
- [asset/](asset/asset.md) · [update](update/update.md)：包资产与唯一写盘通道。
## 快速上手
```
python scripts/deps_check.py              # 依赖自检（初始化第 4 项）
python scripts/check_links.py --root .    # 悬空链接须＝0
python scripts/check_len.py --root .      # 每 .md ≤50 行
python scripts/lint_deps.py --root .      # deps.json 每条含 source_url
python scripts/process_chain.py load      # 续跑中断步骤（失败分诊入口）
```
校验脚本一律带 `--root <skill目录>`（[ST-001](references/编排判例/ST-001-校验脚本参数面漂移.md)）。
## 门禁口径
放行只认**证据四件套**（命令／版本／退出码／原始输出），无证据＝不放行；
失败先分诊（真缺陷／脆弱用例／环境抖动）再定责，禁止靠放宽断言、跳过用例、
调大超时「修绿」（[测试门禁](resistance/测试门禁/测试门禁.md)）。
## 边界
本技能不写被测实现、不执行发布与远端协作、不执行 `planned_tasks/` 本体；
内容变更一律走 [update](update/update.md)（tmp 镜像 → compare → release → clean）。
## 许可与贡献
[MIT](LICENSE) · [CHANGELOG.md](CHANGELOG.md) · [CONTRIBUTORS.md](CONTRIBUTORS.md)
