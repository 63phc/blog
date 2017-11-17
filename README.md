#blog

####theme 
```git
git clone https://github.com/arulrajnet/attila
```

####plugins 
```git
git clone --recursive https://github.com/getpelican/pelican-plugins
```
#### deploy 
```
pelican -s pelicanconf.py
ghp-import output
ghp-import -b gh-pages output
```