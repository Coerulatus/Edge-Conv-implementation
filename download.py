import os

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
  os.mkdir(DATA_DIR)
if not os.path.exists(os.path.join(DATA_DIR, 'modelnet40_ply_hdf5_2048')):
  www = 'https://shapenet.cs.stanford.edu/media/modelnet40_ply_hdf5_2048.zip'
  zipfile = os.path.basename(www)
  os.system('wget %s --no-check-certificate; unzip %s' % (www, zipfile))
  os.system('mv %s %s' % (zipfile[:-4], DATA_DIR))
  os.system('rm %s' % (zipfile))