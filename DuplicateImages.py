from PIL import Image
import imagehash
import os
import sys

def delete_dupes(directory):
    hashSet = set()
    count = 0
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            #print(f"{directory}\{filename}")
            hash = imagehash.average_hash(Image.open(f'{directory}\{filename}'))
            if hash in hashSet:
                os.remove(os.path.join(directory, filename))
                print(f"Deleting file: {filename}")
                count += 1
            else:
                hashSet.add(hash)
    print(f"Deleted {count} duplicate files.")

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("ERROR: Input of the directory is needed.")
    else:
        delete_dupes(sys.argv[1])