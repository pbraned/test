from PIL import Image
import imagehash
import sys

hashmethod = sys.argv[1] if len(sys.argv) > 1 else 0
if hashmethod == 'ahash':
        hashfunc = imagehash.average_hash
elif hashmethod == 'phash':
        hashfunc = imagehash.phash
elif hashmethod == 'dhash':
        hashfunc = imagehash.dhash
elif hashmethod == 'whash-haar':
        hashfunc = imagehash.whash
#elif hashmethod == 'whash-db4':
#       def hashfunc(img):
#               return imagehash.whash(img, mode='db4')
elif hashmethod == 'colorhash':
        hashfunc = imagehash.colorhash
elif hashmethod == 'crop-resistant':
        hashfunc = imagehash.crop_resistant_hash

hash = hashfunc(Image.open(sys.argv[2]))
otherhash = hashfunc(Image.open(sys.argv[3]))
#print(hash)
#print(otherhash)
hamm = hash - otherhash

if hamm <= int(sys.argv[4]):
  print(sys.argv[2] + " and "+ sys.argv[3] + " = "+ str(hamm))  # hamming distance

return(hamm)
