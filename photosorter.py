from PIL import Image
import dhash
import pybktree
import os

def filecleanup(scrpth):
    imagedict = {}
    tree = pybktree.BKTree(pybktree.hamming_distance)


    for ff in os.listdir(scrpth):
        #print(os.path.join(scrpth,ff))
        filename = os.path.join(scrpth,ff)
        if filename[-3:] == "jpg":
            #calc dhash of image
            try:
                image = Image.open(filename)
                dhashint = dhash.dhash_int(image)
                tree.add(dhashint)
                imagedict[dhashint] = filename
            except:
                pass


    for fff in imagedict.keys():
        try:
            print(".")
            os.rename(imagedict[fff], os.path.join(scrpth, "sorted",str(fff)+os.path.basename(imagedict[fff])))

        except:
            print("error with file: " + imagedict[fff])

if __name__ == '__main__':
    ficusroot = r"C:\Users\Owen\Desktop\ficusnitada"
    filecleanup(ficusroot)
    podoroot = r"C:\Users\Owen\Desktop\podocarpus"
    filecleanup(podoroot)




