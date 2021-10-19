# Python Video Compiler
[![](https://img.shields.io/badge/Python-MoviePy-blue)](https://pypi.org/project/moviepy/)

Concat/Merge/Compile video from **urls** using **MoviePy**
<hr>

```
pip install moviepy
```
Usage
```python
from video_compiler import VideoCompiler


vc = VideoCompiler()

url_list = [
    "https://abc.com/abcdefgh_01.mp4",
    "https://abc.com/abcdefgh_02.mp4",
    .
    .
    .
]

vc.load_videos(url_list)
vc.merge_videos()
```
