import dicom
import os
import numpy
#from matplotlib import pyplot, cm

PathDicom = "/home/muhfi/Documents/thesisMuhfi/DiCOM/dataperfusi/"
lstFilesDCM = [] # Create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower(): # Check wether the file's DiCOM
            lstFilesDCM.append(os.path.join(dirName,filename))

# Get ref file
RefDs = dicom.read_file(lstFilesDCM[0])

# Load Dimensions based on the number of rows, columns, and slices (along the Z axis)
print(RefDs.Rows)
print(RefDs.Columns)
print(lstFilesDCM)
ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), len(lstFilesDCM))

# Load spacing values in mm
ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SliceThickness))

#x = numpy.arange(0.0, (ConstPixelDims[0]+1)*ConstPixelSpacing[0], ConstPixelSpacing[0])
#y = numpy.arange(0.0, (ConstPixelDims[1]+1)*ConstPixelSpacing[1], ConstPixelSpacing[1])
#z = numpy.arange(0.0, (ConstPixelDims[2]+1)*ConstPixelSpacing[2], ConstPixelSpacing[2])

# The array is sized based on 'ConstPixelDims'
# ArrayDicom = numpy.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)
ArrayDicom1 = numpy.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)
ArrayDicom2 = numpy.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)

# loop through all the DICOM files
#for filenameDCM in lstFilesDCM:
    # read the file
    #ds = dicom.read_file(filenameDCM)
    #print(ds)
    #raw_input("Press Enter to continue...")
    # store the raw image data
    #ArrayDicom[:, :, lstFilesDCM.index(filenameDCM)] = ds.pixel_array 
    #print(ds.pixel_array)

ds1 = dicom.read_file(lstFilesDCM[1])
ds2 = dicon.read_file(lstFilesDCM[9])

ArrayDicom1[;, ;, ] = ds1.pixel_array
ArrayDicom2[;, ;, ] = ds2.pixel_array
