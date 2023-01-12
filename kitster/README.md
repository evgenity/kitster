### to compress images
find . -name '*.jpeg' -o -name '*.png' -o -name '*.webp' -exec sips -s format jpeg -s formatOptions low {} --out {} \;

## to fix media permissions
chmod -R 770 ./media/