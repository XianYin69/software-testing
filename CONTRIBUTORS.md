# CONTRIBUTORS（software-testing）
## 维护者
- XianYin69：需求方／维护者——定技能范围与约束，负责合并与发布决策。
## 贡献者
- `Skill_Generator`：生成器——提供创建／修改流程、初始化脚本与审查工具链
  （`check_links`／`check_len`／`lint_deps` 均取自其工具面）。
- `general-software-dev`：伞形中枢——以计划任务委派本技能生成，
  五机制／沙盒／降级／git 工作流约束按本技能改名复用（见
  [dependence/dependence.md](dependence/dependence.md)）。
- SMS 执行对话（工具自办）：`branch/` 大纲与分支分析、`references/` 素材库、
  `dependence/deps.json`、根文档（README／CHANGELOG／CONTRIBUTORS）。
- 被派发技能（不并入本仓正文）：`general-programming`／`python-expert`／
  `cpp-expert`／`webapp-testing`／`packaging-and-release`／`git-remote-management`
  ——去向见 [委托边界](resistance/委托边界/委托边界.md)。
## 贡献方式
1. 内容变更一律走 [update/update.md](update/update.md)：tmp 镜像 → compare →
   release → clean，不加 `--yes` 只预览，禁止静默写盘；
2. 约束库（[resistance/](resistance/resistance.md)）与红线区**只可加严**，
   不得放宽或删除（[约束部分](resistance/约束部分/约束部分.md)）；
3. 判例与经验落 [references/](references/references.md)，须绑真实运行记录＋提交号；
4. git：功能分支 → 双链辩论＋悬空链接 0 → dev → 整体审查通过 → main，
   推送前须用户确认（[git工作流约束](resistance/git工作流约束/git工作流约束.md)）；
5. 提 PR／远端协作不在本技能内执行，派 `create-pull-request`。
## 约定
- 文档 ≤ 50 行、脚本英文命名、悬空链接＝0、缓存与运行产物不入 skill 目录；
- 不提交凭据、个人信息、生产数据快照或未授权第三方内容。
## 许可
[MIT](LICENSE)。
