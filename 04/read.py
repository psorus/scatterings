import nibabel as nib
import os

def read(fn):

    img = nib.load(fn)

    return img.get_fdata()

def iterfiles():
    for zw in os.listdir("ct_scans"):
        if not ".nii" in zw:continue
        yield zw,read(f"ct_scans/{zw}")


if __name__=="__main__":
    for fn in iterfiles():
        x=read(fn)
        exit()

