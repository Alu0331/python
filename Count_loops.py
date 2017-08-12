import re
import glob
import os
#for integer

def countloops(file1):
  norfor=0
  nestfor=0
  #print(file1)
  lineno=0
  for line in file1:
    lineno +=1
    normalfor= r'for\s\w+\sin\s.+:$'
    #nesfor = r'^\t{1,}(for)'  # Do not delete 'r'.
    matchfor = re.findall(normalfor, line)
    #matchnes = re.findall(nesfor, i)
    if matchfor:
      print(str(lineno).zfill(3),' '.join(str(x) for x in matchfor))
      norfor +=1
    #elif len(matchnes)==1:
      #nestfor +=1
  return norfor
  #for i in ddas:
  #print("Nested for = ",nestfor)

def isdirectoryorfile(files):
  if os.path.isdir(files):
    for files in glob.glob(files+"/*"):
      isdirectoryorfile(files)
  elif files.endswith('.py'):
    file1 = open(files)
    print(os.path.basename(files))
    Totalloop = countloops(file1)
    print("Total for loops = ",Totalloop,"\n")
    file1.close()

Totalloop=0
for files in glob.glob("C:/Users/hp/Google Drive/*"):
    isdirectoryorfile(files)
