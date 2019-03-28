import sys
import os
import json

# convert invalided character in name of file to chinese character
def file_format(str):
    lt="\\/:*?\"<>|"
    for i in lt:
        if str.find(i) != -1:
            str=str.replace(i,chr(ord(i)+65248))
    return str

def main():
    if len(sys.argv)==2:
        path=sys.argv[1]
        output=""            # ouput path
        videoName=""
        videoId=0
        idWidth=len(str(len(os.listdir(path))))
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                if 'entry.json' in files:
                    with open(root+'\\'+'entry.json', encoding='utf8') as f:
                        entry=json.load(f)
                        output=file_format(entry['title'])
                        if os.path.exists(output) is False:
                            os.makedirs(output)
                        videoName=file_format(entry['page_data']['part'])
                        videoId=entry['page_data']['page']
                elif 'index.json' in files:
                    fileList=list(filter(lambda file:file.endswith('.blv'), files))
                    sorted(fileList)
                    tempFile=r'filelist'
                    with open(tempFile, 'w') as f:
                        for file in fileList:
                            f.write('file \'%s\\%s\'\n' % (root, file))
                    cmd='ffmpeg -v warning -f concat -safe 0 -i \"%s\" -c copy \"%s\\%0*d.%s.flv\" -hide_banner' % (tempFile, output, idWidth, videoId, videoName)
                    os.system(cmd)
                    os.remove(tempFile)

main()