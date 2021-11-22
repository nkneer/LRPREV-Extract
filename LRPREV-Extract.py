# ----- Begin configuration section -----

# You need to tell the program two things:
#   1. PathRead: Where your preview files are
#   2. PathWrite: Where you want to save the extracted JPEG files 
PathRead = 'C:/extract/from/'
PathWrite = 'C:/extract/to/'
# ----- End configuration section -----

# ----- Begin program section -----
import os
PreviewFilesArray = []
for path, subdirs, files in os.walk(PathRead):
    for file in files:
        if file.endswith(".lrprev"):
            PreviewFilesArray.append(os.path.join(path, file))
i = 0
for PreviewFile in PreviewFilesArray:
    with open(PreviewFile, "rb") as CurrentFile:
        CurrentFileRead = CurrentFile.read()
        ExtractedJPGData = CurrentFileRead.split(bytes("level_", "ANSI"))[-1]
        CurrentFileByteArray = bytearray(ExtractedJPGData)
        del CurrentFileByteArray[0:2]
        with open(PathWrite + str(i) + ".jpg", "wb") as ExtractedJPGFile:
            ExtractedJPGFile.write(bytes(CurrentFileByteArray))
            i = i + 1
