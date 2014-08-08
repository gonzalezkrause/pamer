#!/usr/bin/env python
#-*- coding: utf-8 -*-

from os.path import join
from base64 import b64encode
from sys import argv, exit


def getOpts():
   if len(argv) < 4:
      print('Usage:')
      print('{0} name_file_a name_file_b output_file inBase64'.format(argv[0]))
      print('{0} passwds1.txt passwds2.txt true'.format(argv[0]))
      exit(1)
   else:
      global b64
      b64 = False
      finAName = argv[1]
      finBName = argv[2]
      foutName = argv[3]
      if len(argv) >= 5:
         b64 = True

   return(finAName, finBName, foutName)


def openFiles(opts):
   f1 = None
   f2 = None
   f3 = None
   with open(opts[0], 'r') as f:
      f1 = f.read()
   with open(opts[1], 'r') as f:
      f2 = f.read()
   f3 = open(opts[2], 'w')
   return(f1, f2, f3)


def merger(fileA, fileB):
   mergedPasswds = ''
   listA = [word for word in fileA.split('\n')]
   listB = [word for word in fileB.split('\n')]
   print('[*] Generatin a list with {0} elements'.format(len(listA) * len(listB)))
   for u in listA:
      for p in listB:
         if b64:
            mergedPasswds += b64encode('{0}:{1}'.format(u, p)) + '\n'
         else:
            mergedPasswds += '{0}:{1}\n'.format(u, p)
   return mergedPasswds


if __name__ == '__main__':
   try:
      opts = getOpts()
      files = openFiles(opts)
      endFile = merger(files[0], files[1])
      files[2].write(endFile)
      files[2].close()
   except Exception, e:
      print('[*] {0}'.format(e))
   except KeyboardInterrupt:
      print('Bye!')

