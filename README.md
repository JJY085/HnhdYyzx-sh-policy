# 上海电力市场政策学习地图

静态政策知识库：国家 1+6 基础规则、华东/长三角区域规则、上海地方政策。支持独立详情页、全文搜索、五维筛选、政策关系、状态标记和移动端布局。

## 开发

需要 Node.js 20 或更新版本，无第三方运行依赖。

```sh
npm run build
npm test
npm run dev
```

## 部署到 Vercel

在 Vercel 中导入 `JJY085/HnhdYyzx-sh-policy`，Framework 选择 Other。构建命令为 `npm run build`，输出目录为 `dist`。仓库内 `vercel.json` 已配置。连接 GitHub 后，推送 main 自动触发部署。不需要环境变量、数据库或服务器。

## 维护数据

直接编辑 `src/data/policies.json` 和 `src/data/policy-relations.json`。新增政策后构建会生成详情页及搜索数据。不要重新运行导入脚本覆盖已核验内容；导入脚本仅记录首次数据迁移流程。

缺失字段使用 null；官方链接与核验范围需要保留。新增版本使用独立 ID 和 `supersedes` / `superseded_by`，旧版本保留并改为历史状态。主体标签仅用于检索，不等于准入资格。

## 核验边界

核验日期为 2026-09-12。已读取官方发布页，补充部分成文日期、实施日期、文号、附件和核心摘要；核验范围逐条显示。上海现货动态预览无法读取，具体版本仍待核验。上海中长期附件较大，已核对官方目录与文件链接，但没有完成逐条全文核验。正文以原始项目资料为基础，学习摘要不替代官方文件。

## GitHub Pages

本次发布使用 `gh-pages` 分支根目录的构建产物。项目地址为 https://jjy085.github.io/HnhdYyzx-sh-policy/ 。

```sh
BASE_PATH=/HnhdYyzx-sh-policy npm run build
BASE_PATH=/HnhdYyzx-sh-policy npm test
```

将 `dist/` 的内容发布至 `gh-pages` 分支根目录即可更新网站。当前 `main` 仅保存源码，单独推送源码不会更新 Pages；需重新构建并发布产物。未设置 BASE_PATH 时仍适用于根域名托管。
