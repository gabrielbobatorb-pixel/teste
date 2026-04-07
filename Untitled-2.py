print("meu primeiro commit")
git config --global user.name "Gabriel Bobato"
git config --global user.email "gabrielbobato.rb@gmail.com"
git remote add origin https://github.com/gabrielbobatorb-pixel/teste.git
git branch -M main
git add .
git commit -m "Meu primeiro commit do script Python"
git push -u origin main