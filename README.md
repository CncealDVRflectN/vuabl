# Visualizer for Unity Addressables build layout [![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

*Visualizer for Unity Addressables build layout* or just *vuabl* is a small app, that tries to simplify the task of optimizing the build size in Unity projects with the [Addressables system](https://docs.unity3d.com/Packages/com.unity.addressables@1.18/manual/index.html)

## Requirements
- Python 3.6 or higher
- pip

## Installation

On Windows:
```bash
pip install vuabl
```
Or:
```bash
py -m pip install vuabl
```

On other systems:
```bash
pip3 install vuabl
```
Or:
```bash
python3 -m pip install vuabl
```

## Usage
Simply run:
```bash
vuabl your_buildlayout.txt
```

Then open the app address in your browser (by default it is [127.0.0.1:8050](http://127.0.0.1:8050/))

Example:

![Example](https://media3.giphy.com/media/TeLeBQcSw1JoUSyl2o/giphy.gif?cid=790b76118ea89de73c74b1dfe6549074161497e763dc0399&rid=giphy.gif&ct=g)

If you don't know how to generate an Addressables build layout or where to find it, [check this](https://docs.unity3d.com/Packages/com.unity.addressables@1.18/manual/BuildLayoutReport.html#creating-a-build-report)

## Options
Your can get a list of all supported options by adding *-h* or *--help* to the command. For example:
```bash
vuabl -h
```
