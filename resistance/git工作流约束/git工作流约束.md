# git 工作流约束

本技能（software-testing）与其编排的项目仓库共用同一分支纪律。

## 规则

1. **启动前拉取**：动手前 `git fetch`，有更新先 `git pull --ff-only`。
2. **功能分支提交**：每步完成在 `feature/<topic>` 提交（步骤名入分支名，英文）。
3. **审核通过→dev**：双链辩论通过＋悬空链接＝0 后，功能分支合入 `dev`。
4. **整体审查通过→main**：九项标准全绿后 `dev` 合入 `main`，`main`＋`dev` 一起推送。
5. **禁止直写 main/dev**：二者不接受直接 commit。
6. **重试熔断**：审查失败重试达 10 次触发 penalty 熔断，回退功能分支或求助用户。
7. **忽略清单**：`.gitignore` 必含 `tmp/` 与 IDE 目录（`.idea/`、`.vscode/`、`.kilo/`）。
8. **自动 git init**：无 `.git` 即先 `git init`，不得跳过。
9. **推送前确认**：必须经用户确认才可 `git push`。
10. **仓库可见性**：可能侵权/危害社会/涉嫌违法或含用户须保密内容的仓库必须 PRIVATE，
    其余 PUBLIC；判不了就问用户，不得擅自设 PUBLIC。
11. **附属技能双仓**：附属/私有子技能（前缀如 `software_use_only-*`）同样必须进 git，
    进的是宿主目录下 `private/` 工作树的**独立私有伴生仓**（PRIVATE）；
    本体仓 PUBLIC 且 ignore `private/`（仅留 `.gitkeep`）；私有内容出现在公开仓＝泄漏
    `E_LEAK_TO_PUBLIC`；可见性由仓库属性＋register.json＋脚本校验承载，
    **禁止在 SKILL.md frontmatter 自造 visibility 字段**；只注册不发布视为未完成。

## 相关

- [resistance](../resistance.md) · [../../SKILL.md](../../SKILL.md)
- [收尾 git 节点](../../branch/收尾/收尾.md) · [审查约束](../审查约束/审查约束.md)
