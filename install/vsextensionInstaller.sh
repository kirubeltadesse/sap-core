echo "Installing Visual Studo Code extensions"

for extension in $(cat extensions)
do 
    echo "Installing: ${extension}"
    code --install-extension $extension
done