# Problem Set 1 - Read the data files
# Adrian Golias
# Importing libraries
import gzip
import binascii

# Declaration of variables for images and labels
# and stating the path to open correspondant files
images = gzip.open('data/train-images-idx3-ubyte.gz', 'rb')
labels = gzip.open('data/train-labels-idx1-ubyte.gz', 'rb')

# Read images from the file location
imageMagic = images.read(4)
# Print images
print(imageMagic)
# Read images byte by byte
readImageBytes = int.from_bytes(imageMagic, byteorder="big")
# Print image bytes
print(readImageBytes)
# Close image path
images.close()

# Read labels from the file location
labelMagic = labels.read(4)
# Print labels
print(labelMagic)
# Read labels byte by byte
readLabelBytes = int.from_bytes(labelMagic, byteorder="big")
# Print label bytes 
print(readLabelBytes)
# Close label path
labels.close()