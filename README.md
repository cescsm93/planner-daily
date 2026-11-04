# 规划师早报

面向规划从业者的每日简报静态站点，四个栏目：论文、政策、案例、AI 工具。线上地址：[https://planner-daily-pi.vercel.app](https://planner-daily-pi.vercel.app)。

## 文件布局

- `template.html`：页面模板。
- `build.py`：把 `data/` 里最新一期 JSON 嵌入模板，生成 `index.html`。
- `index.html`：当前已构建的页面。
- `data/YYYY-MM-DD.json`：每日一期，一期一个文件。
- `.vercelignore`：部署时忽略源文件与截图。
- `screenshot-*.png`：页面截图。

## 重新构建

在仓库根目录执行：

```bash
python3 build.py
```

## 每日更新

目前由自动化助手完成：写入 `data/<日期>.json`，运行 `python3 build.py`，再部署到 Vercel。
