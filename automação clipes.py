import os
import shutil

o = r'C:\Users\luyzp\Videos\EaseUS RecExperts'
d =  r'C:\Users\luyzp\Videos\Captures\eafc 25 02'

for a in os.listdir(o):
    if a.endswith('.mp4'):
        shutil.move(o + '\\' + a, d + '\\' + a)

print('Clipes movidos!')