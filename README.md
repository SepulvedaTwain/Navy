# Navy

Navy is a small tool to move fast through directories in Linux or Windows, especially helpful when playing with helm charts.

## Make alias
```cd ~```, edit .bashrc and add at the bottom:
```
export PATH=$PATH:<your/path>/Navy
alias navy='navy.py'
```
Then, ```source .bashrc``` and you are ready.


## How to use
Navy default path is from where it is executed, that can change with ```-p <your/path>``` or ```--path <your/path>```.
Run Navy, then type the characters next to the directory you want to go to and it automatically moves you.
Example:
```bash
Sepulveda@Sepulveda-VirtualBox:~/Desktop$ navy -p ./Example/
|~/   
|~Dir2/   
  |-somefile
  |-text.txt
  |~SubDir1/   stw
     |-somefile
     |-text.txt
     |~SubSubDir2/   ywx
        |-another_file
     |~SubSubDir1/   lb
  |~SubDir2/   ci
     |-another_file
|~Dir3/   
  |-somefile
  |~SubDir1/   db
|~Dir1/   
  |-somefile
  |-text.txt
  |~SubDir1/   nb
  |~SubDir2/   yzu
     |-another_file
Type shortcut or q to quit.. :       # ywx was typed
Sepulveda@Sepulveda-VirtualBox:~/Desktop$ cd Example/Dir2/SubDir1/SubSubDir2
Sepulveda@Sepulveda-VirtualBox:~/Desktop/Example/Dir2/SubDir1/SubSubDir2$ 
```
You can manipulated how many levels of subdirs you want to print (default is 4) with ```-l``` or ```--level```, or if you want all the level run with ```-a-``` or ```--all```.

If you only want to view the _Directories_ run with ```-d``` or ```--directories``` (really helpful).

Sometimes it's not convenient to print all the directories and file. You can run navy with ```-c``` or ```--control``` to print only 15 at a time, so you won't have to scroll up. To print more just type **n** (also really helpful).

Example:
```bash
Sepulveda@Sepulveda-VirtualBox:~/Desktop$ navy -p ./Example/ -c -d
Type shortcut, n to continue or q to quit.. : 
|~/   
|~Dir2/   
  |~SubDir1/   bf
     |~SubSubDir2/   xsu
     |~SubSubDir1/   en
  |~SubDir2/   zzs
     |~SubSubDir2/   top
        |~SubSubDir2/   zrz
           |~SubSubDir2/   tuz
           |~SubSubDir1/   wry
        |~SubSubDir1/   rux
           |~SubSubDir2/   cd
           |~SubSubDir1/   ec
     |~SubSubDir1/   fe
|~Dir3/   
  |~SubDir1/   mi         # n was pressed
     |~SubSubDir2/   dd
        |~SubSubDir2/   ssz
        |~SubSubDir1/   yxy
           |~SubSubDir2/   opo
           |~SubSubDir1/   rzx
     |~SubSubDir1/   oyp
|~Dir1/   
  |~SubDir1/   xrx
  |~SubDir2/   wyu
|~Dir4/   
  |~MoreDirs/   im
     |~SubSubDir2/   mb
        |~SubSubDir2/   lm
        |~SubSubDir1/   dg
           |~SubSubDir2/   vsv
           |~SubSubDir1/   kd     # lm was typed
 
Sepulveda@Sepulveda-VirtualBox:~/Desktop$ cd ./Example/Dir4/MoreDirs/SubSubDir2/SubSubDir2
Sepulveda@Sepulveda-VirtualBox:~/Desktop/Example/Dir4/MoreDirs/SubSubDir2/SubSubDir2$ 


```

For help ```navy -h``` or ```navy --help```:

```bash
$ navy -h
usage: nav.py [-h] [-p PATH] [-l LEVEL] [-a] [-d] [-c]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Prints from the path you want to navigate from.
  -l LEVEL, --level LEVEL
                        Prints x levels. Default is 4.
  -a, --all             Prints the whole tree.
  -d, --directories     Prints only directories.
  -c, --control         Prints 15 directories and with n the next 15 etc.
```
