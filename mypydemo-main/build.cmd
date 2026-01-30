pyinstaller mypydemo.spec
pandoc --to HTML README.md -o dist\mypydemo\README.html
copy LICENSE.txt dist\mypydemo
pushd dist
7z a mypydemo.zip mypydemo
popd
