import os
import requests
from moviepy.editor import *
from datetime import datetime


class VideoCompiler:
    def __init__(self, file_name='TEMP'):
        parent_dir = 'video'
        video_dir = f"{parent_dir}/{file_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        self.video_dir = video_dir
        if not os.path.isdir(parent_dir):
            os.mkdir(parent_dir)
        os.mkdir(video_dir)

        self.output_file = f'{video_dir}.mp4'
        self.video_clips = []
        self.video_paths = []

        self.size = (1920, 1080)
        self.vert_offset = 40
        self.fps = 60

    # -----------------------------------------------------------------------------------------------------------------------

    def merge_videos(self, delete_source=True):
        merge_clip = concatenate_videoclips(
            self.video_clips, method="compose").set_position("center")

        back_clip = ColorClip(size=self.size, color=(
            255, 255, 255), duration=merge_clip.duration)

        CompositeVideoClip([back_clip, merge_clip]).write_videofile(
            self.output_file, threads=4, logger=None, write_logfile=False)

        if delete_source:
            for video_file in self.video_paths:
                os.remove(video_file)
            os.rmdir(self.video_dir)

        return {'output_file': self.output_file}

    # -----------------------------------------------------------------------------------------------------------------------

    def load_videos(self, url_list):
        for link in url_list:
            file_path = f"{self.video_dir}/{link.split('/')[-1]}"

            if file_path not in self.video_paths:
                self.video_paths.append(file_path)
                r = requests.get(link, stream=True)
                with open(file_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024*1024):
                        if chunk:
                            f.write(chunk)

        self.video_clips = [VideoFileClip(path).resize(
            height=self.size[1]-self.vert_offset).set_fps(self.fps) for path in self.video_paths]

        return {'video_dir': self.video_dir}
