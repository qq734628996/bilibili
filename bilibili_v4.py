import argparse
import sys
import os
import json
import shutil


def windows_file(file):
    for i in '\\/:*?\"<>|':
        file = file.replace(i, chr(ord(i)+65248))
    return file


def extract(args):
    path = args.input
    id_digit = len(str(len(os.listdir(path))))
    for root, dirs, files in os.walk(path):
        if 'entry.json' in files:
            with open(os.path.join(root, 'entry.json'), encoding='utf8') as f:
                entry = json.load(f)
                video_name = windows_file(entry['page_data']['part'])
                video_id = entry['page_data']['page']
                path_base = windows_file(entry['title'])
                if not os.path.exists(path_base):
                    os.makedirs(path_base)
                if args.number:
                    video_name = f'{video_id:0{id_digit}}.{video_name}'
                path_danmu = os.path.join(root, 'danmaku.xml')
                if os.path.exists(path_danmu):
                    shutil.copy(path_danmu, os.path.join(
                        path_base, f"{video_name}.xml"))
        elif 'index.json' in files:
            path_video = os.path.join(root, 'video.m4s')
            path_audio = os.path.join(root, 'audio.m4s')
            path_output = os.path.join(path_base, f'{video_name}.mp4')
            cmd = f'ffmpeg -v warning -y -i "{path_video}" -i "{path_audio}" -c copy "{path_output}"'
            os.system(cmd)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        '--number',
        help='add prefix number to each file.',
        action='store_true',
    )
    parser.add_argument(
        '-i',
        '--input',
        help='input path(default all folders in current path).',
    )
    args = parser.parse_args()
    if args.input:
        extract(args)
    else:
        for i in os.listdir('.'):
            if os.path.isdir(i):
                args.input = i
                extract(args)


if __name__ == "__main__":
    main()
