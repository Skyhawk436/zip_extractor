import zipfile, os

print("+ ----------------------------------------------------")
print("+                                                    +")
print("+                  Zip file extractor                +")
print("+                                                    +")
print("+ ----------------------------------------------------")
print("\n\n")

inputFolder = input(r"path to zip folders to extract:")
print("\n")
outputFolder = input(r"path to extraction folder:")
print("\n")

os.chdir(inputFolder)
num_files = 0

for file in os.listdir():

    if zipfile.is_zipfile(file):
        print("Extracting: " + file)
        z = zipfile.ZipFile(file)
        z.extractall(outputFolder)
        z.close()
        num_files += 1
    else:
        print(' \"{}\" is not a zip file'.format(file))

print("\n\n")
print("\nDone!")
print(str(num_files) + " zip folders extracted")
