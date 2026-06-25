# 场景综述：建模与BIM

> 文档日期：2026-06-12 v3.0
> 目的：从设计师、产品、技术三层视角整合建模+BIM协同场景（原 建模 + BIM协同 合并）

## 一、设计师视角：AI 建模能做什么

### 建模 AI 能力矩阵

| 能力 | 成熟度 | 代表工具 |
|---|---|---|
| **图转 3D**（照片/草图→3D 模型） | ⚠️ 可用但不精确 | 3DFY.ai, Ponzu.gg |
| **卫星图→城市 3D** | ✅ 成熟（LOD 1-2） | BlackShark AI |
| **AI 生成 PBR 材质** | ✅ 成熟 | Adobe Substance 3D |
| **点云→3D 网格** | ✅ 可用 | PointFuse, Metascan |
| **Web 参数化生成** | ✅ 可用 | Hypar |
| **MCP 自然语言建模** | ⚠️ 实验性 | BlenderMCP, RhinoMCP |
| **AI 从零创建建筑模型** | ❌ 极早期 | — |

### BIM 协同的四层含义

| 层级 | 内容 | 代表工具 | 建筑师参与度 |
|---|---|---|---|
| **数据互操作** | Revit↔Rhino↔GH 数据互通 | Speckle | 中 |
| **多人协作** | 多人同时编辑同一个 BIM 模型 | BIM 360/ACC | 高 |
| **施工对比** | BIM 模型 vs 工地现场 AI 对比 | Constru | 低 |
| **AI 预警** | 项目风险 AI 预测 | Construction IQ | 低 |

### 建筑师最实际的两个需求

1. **"我的 Rhino 模型怎么给 Revit 的同事用？"** — Speckle 是唯一解决此问题的开源工具
2. **"为什么每次模型改了都要重新导出/导入？"** — 数据流（非文件）是答案

## 二、产品视角：建模+BIM 赛道格局

### 产品矩阵

| 工具 | 形态 | AI 成分 | 开放度 |
|---|---|---|---|
| Rhino + GH | 桌面 NURBS | ⚠️（Raven GH AI Assist） | 闭源 |
| Revit | 桌面 BIM | ⚠️ | 闭源 |
| Speckle | 开源 3D 数据流 | ❌ | ✓ 开源 |
| Hypar | Web 参数化 | ✅ | ✓ 开源核心 |
| BricsCAD BIM | 桌面 DWG 原生 | ✅（AI 辅助） | 闭源 |
| Constru | Web 施工对比 | ✅ | 闭源 |
| Construction IQ | 企业 AI 预警 | ✅ | 闭源 |
| BlenderMCP / RhinoMCP | MCP 协议插件 | ✅ | ✓ 开源 |

### 天然壁垒

建模是"设计中间件"，建筑师在 Rhino/SU/Revit 里已形成根深蒂固的工作流。桌面端 3D 引擎开发（NURBS/BIM 数据模型）与轻量级 Web AI 工具的技术栈差异很大。Speckle 的数据连接器是比自建建模工具更务实的方案。

## 三、技术视角：AI 3D 生成 + 数据流

### AI 3D 生成的三条路线

| 路线 | 技术 | 适合建筑？ |
|---|---|---|
| **NeRF/Gaussian Splatting** | 多照片→3D 场景重建 | ⚠️ 外立面/室内扫描 |
| **AI Mesh/Point Cloud 生成** | 文本→扩散模型→3D | ❌ 精度不够建筑级 |
| **程序化/参数化生成** | 规则+算法→几何 | ⚠️ 方盒子可以，复杂造型难 |

### BIM 协同的技术进化

```
Gen 1：文件传递 → .rvt/.ifc/.3dm 传来传去
Gen 2：中心文件 → BIM 360/ACC 工作共享
Gen 3：开放数据流 → Speckle API 流式实时同步
```

### MCP 协议对建模的影响

BlenderMCP 和 RhinoMCP 通过 MCP 协议让 AI 编程工具（Claude Code/Cursor）能用自然语言操控 3D 软件。该方向仍处于观察中：它可能降低参数化设计门槛，但稳定性、可控性和建筑级精度还需要持续验证。

## 信息来源与时效性

整合自原场景综述和已有评测：
- [Hypar](./Hypar.md) | [BlackShark AI](./BlackShark_AI.md) | [Adobe Substance 3D](./Adobe_Substance_3D.md)
- [Speckle](./Speckle.md) | [Construction IQ](./Construction_IQ.md) | [Constru](./Constru.md)

## 更新记录
- 2026-06-12：从原 场景综述_建模.md + 场景综述_BIM协同.md 合并升级为 v3.0
