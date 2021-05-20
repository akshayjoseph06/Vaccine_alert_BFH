import os
os.system('cmd /k "ffmpeg -i test.mp3 -filter_complex "[0:a]showwaves=s=1280x720:mode=cline,format=yuv420p[v]" -map "[v]" -map 0:a -c:v libx264 -c:a copy test.mp4"') # 128x96
