from rembg import remove
from PIL import Image
import sys
import os

def remove_background(input_path, output_path):
    with open(input_path, 'rb') as inp_file:
        input_image = inp_file.read()
    output_image = remove(input_image)

    with open(output_path, 'wb') as out_file:
        out_file.write(output_image)

    print(f"[Done ✅] Background removed: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_bg.py input.jpg output.png")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if not os.path.exists(input_file):
        print(f"[❌] File not found: {input_file}")
        sys.exit(1)
    remove_background(input_file, output_file)
