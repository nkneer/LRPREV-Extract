import os


# Configuration section
PathRead = 'C:\\Users\\nknee\\Desktop\\Lightroom\\' #Set to the path where your previews are
PathWrite = 'C:\\extract\\to\\' #Set to the path you want your extracted JPEGs to be
# end of configuration section


# Begin program section
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
