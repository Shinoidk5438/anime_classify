# 赛博插画鉴定师——帮您一眼丁真分辨冻鳗插画和杂鱼
## 说明

本项目模型基于 `yolov8m-cls` 模型(v8.20)训练

本项目提供 `best.pt` `best.onnx` 两个模型，其中onnx格式可显著提升CPU的运行效率，pt格式为原始格式，可自行导出。

模型会将图片分为三类

- anime: 冻鳗插画
- others: 不是冻鳗插画

## 使用

- 从 [release](https://github.com/Shinoidk5438/anime_classify/releases) 下载训练好的模模型

- 将测试图片放入 `test_img` 目录下

- 安装依赖

  ```bash
  pip install -r requirements.txt
  ```

- 运行 `main.py`

  ``` bash
  python ./main.py
  ```
## 鸣谢

感谢 [ultralytics](https://github.com/ultralytics/ultralytics) 提供yolov8预训练模型

感谢 [所有贡献者](https://github.com/ravizhan/screenshot_classify/graphs/contributors)，无论您是提供了图片或是代码
感谢 [灵感来源及数据来源](https://github.com/ravizhan/screenshot_classify/)，本项目在others类中采用了来自该项目的数据集

## 协议

本项目在带有 [附加条款](https://github.com/ravizhan/screenshot_classify/LICENSE) 的情形下，遵循 [AGPL-3.0协议](https://github.com/ravizhan/screenshot_classify?tab=License-1-ov-file) 开源，请自觉遵守。
