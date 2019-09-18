import argparse
import sys
import os
import json

def windows_file(file):
    for i in '\\/:*?\"<>|':
        file=file.replace(i,chr(ord(i)+65248))
    return file

def run(path,add_number,**kw):
    id_width=len(str(len(os.listdir(path))))
    for root, dirs, files in os.walk(path):
        if 'entry.json' in files:
            with open(os.path.join(root,'entry.json'), encoding='utf8') as f:
                entry=json.load(f)
                path_main=windows_file(f"{entry['title']} [avid: {entry['avid']}]")
                if not os.path.exists(path_main):
                    os.makedirs(path_main)
                video_name=windows_file(entry['page_data']['part'])
                video_id=entry['page_data']['page']
        elif 'index.json' in files:
            path_video=os.path.join(root,'video.m4s')
            path_audio=os.path.join(root,'audio.m4s')
            if add_number:
                path_output=os.path.join(path_main,'{0:0{1}}.{2}.mp4'.format(video_id,id_width,video_name))
            else:
                path_output=os.path.join(path_main,f"{video_name}.mp4")
            cmd=f'ffmpeg -v warning -y -i "{path_video}" -i "{path_audio}" -c copy "{path_output}"'
            os.system(cmd)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        help='Add number before file name.',
        action='store_true',
        dest='add_number'
    )
    parser.add_argument(
        '-i',
        help='Specify the input path. The default is to convert all folders in the current path',
        dest='input_path'
    )
    args=parser.parse_args()
    if args.input_path:
        run(args.input_path,**args.__dict__)
    else:
        for dir in os.listdir('.'):
            if os.path.isdir(dir):
                run(dir,**args.__dict__)

if __name__ == "__main__":
    main()