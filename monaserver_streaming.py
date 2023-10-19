from time import *
import os
import shutil
import subprocess
import threading
knownStreams = []
open('MonaServer_Win64/MonaServer.log/0.log', 'w').close()
def convert(name, folder):
    command = f"ffmpeg -i rtmp://127.0.0.1/live/{name} -c:v copy -c:a copy -bufsize 1835k -pix_fmt yuv420p -flags -global_header -hls_time 10 -hls_list_size 6 -start_number 1 {folder}/video.m3u8"
    os.system(command)
def start():
    subprocess.Popen("cd MonaServer_Win64 && start cmd /C MonaServer.exe",shell=True)
    #os.system('""')
def checkStreams():
    with open('MonaServer_Win64/MonaServer.log/0.log', 'r') as stream:
        line = stream.readlines()
        #print(line)
        for i in line:
            if " Publication " in i:
                i = i.split()
                if i.index("Publication") == 5:
                    name = i.pop(6)
                    try:
                        state = i.pop(14)
                    except:
                        state = i.pop(6)
                    dati = f'{i.pop(0)}-{i.pop(0)}'
                    if f'{name}-{state}-{dati}' not in knownStreams:
                        print(f'{dati}: {name} {state}')
                        knownStreams.append(f'{name}-{state}-{dati}')
                        folder = f'MonaServer_Win64/www/data/{dati.replace("/", ".").replace(":",".")}-{name}'
                        if not os.path.exists(folder):
                            if state == "started":
                                os.mkdir(folder)
                                print(folder)
                                shutil.copy('MonaServer_Win64/main.html', f'{folder}/view.html')
                                with open(f'{folder}/view.html', 'r+') as html:
                                    context = html.read()
                                    context = context.replace("http://localhost/data/video.m3u8",
                                                              f'http://localhost/{folder.replace("MonaServer_Win64/www/", "")}/video.m3u8')
                                    html.seek(0)
                                    html.write(context)
                                    html.truncate()
                                x = threading.Thread(target=convert, args=(name,folder))
                                x.start()
                                print(f'{dati}: {name} converting')
                                with open("MonaServer_Win64/index.html", 'r+') as html:
                                    context = html.read()
                                    nr = int(context.count("hls-example") / 2)
                                    context = context.replace(f"<!---NewVideo--->",
                                                              f'<!---NewVideo---> \n    <video id="hls-example{nr}" class="video-js vjs-default-skin" width="400" height="300" controls> \n        <source type="application/x-mpegURL" src="http://localhost/{folder.replace("MonaServer_Win64/www/", "")}/video.m3u8">\n    </video> \n    <br>\n    <p>{dati.replace("/", ".").replace(":",".")}-{name}<p>\n    <br>')
                                    context = context.replace(f"<!--NewPlayer-->",
                                                              f"<!--NewPlayer--> \n        var player = videojs('hls-example{nr}');\n        player.play();")
                                    html.seek(0)
                                    html.write(context)
                                    html.truncate()
                    #print(name)
                    #print(state)
                    #rint(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    y = threading.Thread(target=start,daemon=True)
    y.start()
    while True:
        checkStreams()
        sleep(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
