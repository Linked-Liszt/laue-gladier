import time
import shutil
import os
import json
import shutil

DELAY = 72

base_dir = '/data34b/Run2023-1/Sheyfer223_CodedAperture/Ni2_mask'
staging_dir = '/clhome/EPIX34ID/dev/src/experiment_staging'

images = os.listdir(base_dir)
images = sorted(images, key=lambda x: int(x.split('.')[0].split('_')[-1]))

completed_fp = '/clhome/EPIX34ID/dev/src/completed_ims.json'
with open(completed_fp, 'r') as comp_f:
   completed_ims = json.load(comp_f)

prev_im = None
for im in images:
    if im in completed_ims:
        continue
    print(f'copying: {im}')
    
    if prev_im is not None:
        os.remove(prev_im)
    prev_im = os.path.join(staging_dir, f'consgeo_{im}')
    shutil.copy(os.path.join(base_dir, im), os.path.join(staging_dir, f'consgeo_{im}'))
    
    completed_ims[im] = True

    with open(completed_fp, 'w') as comp_f:
        json.dump(completed_ims, comp_f)
    
    print('waiting')

    time.sleep(DELAY)
    

