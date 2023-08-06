import subprocess


class ThumbnailImageExtractor:
    @staticmethod
    def run(video_file_name: str, image_file_name: str) -> None:
        subprocess.run(["./ffmpeg", "-y", "-ss", "00:00:10", "-i", video_file_name, "-vframes", "1", image_file_name])
