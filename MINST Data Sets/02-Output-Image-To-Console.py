# Problem Set 2 - Output image to the console
# Adrian Golias

# Importing libraries
import gzip
import binascii

# A function to read the labels from defined file location
def read_labels_from_file(filename):
	# Open zip file 
    with gzip.open(filename, 'rb') as file:
        # Get the magic number
        magic = file.read(4)
        magic = int.from_bytes(magic, 'big')
		# Output the magic number
        print("Magic is: ", magic)
        # Get the number of labels
        numLabels = file.read(4)
        numLabels = int.from_bytes(numLabels, 'big')
		# Output number of labels to console
        print("Number of labels: ", numLabels)
        # Read the labels into data structure
        labels = [file.read(1) for i in range(numLabels)]
        labels = [int.from_bytes(label, 'big') for label in labels]
		
		# Return labels when function is called
        return labels

# A function to read the images from defined file location
def read_images_from_file(filename):
	# Open zip file
    with gzip.open(filename, 'rb') as file:
        # Get the magic number
        magic = file.read(4)
        magic = int.from_bytes(magic, 'big')
		# Output the magic number
        print("Magic is: ", magic)
        # Get the number of images
        numImages = file.read(4)
        numImages = int.from_bytes(numImages, 'big')
		# Output number of images to console
        print("Number of images: ", numImages)
        # Number of rows
        numRows = file.read(4)
        numRows = int.from_bytes(numRows, 'big')
		# Output number of rows to console
        print("Rows: ", numRows)
        # Number of columns
        numColumns = file.read(4)
        numColumns = int.from_bytes(numColumns, 'big')
		# Output number of columns to console
        print("Columns: ", numColumns)
		
		# Declaration of an image array
        images = []
		
		# Loop structure to itterate through images
        for i in range(numImages):
			# Rows array
            rows = []
			# Loop structure to itterate through image rows
            for j in range(numRows):
				# Columns array
                cols = []
				# Loop structure to itterate through image columns
                for k in range(numColumns):
					# Append column
                    cols.append(int.from_bytes(file.read(1), 'big'))
				# Append each column in the row
                rows.append(cols)
			# Append rows in the image 
            images.append(rows)
			
		# Return image
        return images

# Declaration of file variables with corresponding path
train_labels = read_labels_from_file('data/train-labels-idx1-ubyte.gz')
test_labels = read_labels_from_file('data/t10k-labels-idx1-ubyte.gz')
train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')
test_images = read_images_from_file('data/t10k-images-idx3-ubyte.gz')

# Outputing third image in the training set to the console
# Done by representing any pixel value less than 128 as a 
# full stop and any other pixel value as a hash symbol.
# Should output # 2
# Loop structure to itterate through every row of each training image
for row in train_images[4999]:
	# Loop structure to itterate through each column of that row
	for col in row:
		# For every 128th column output '#' symbol, otherwise output '.' symbol
		print('.' if col <= 127 else '#', end='')
	# Output image to conole
	print()