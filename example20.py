# Encrypt your-files.py
#-----------------------------------------------------
import marshal
print ("===========================================")
print ("  Encrypted work_files TOOL beta:ver1.1")
print ("===========================================")
myFile = input('Please Write file path, then press Enter: ')
print ("===========================================")

open_file = open(myFile, 'r').read()
compile_file = compile(open_file, '', 'exec')
encrypt = marshal.dumps(compile_file)
code = open('New_'+str(myFile), 'w')
code.write("import marshal\n")
code.write('exec(marshal.loads('+repr(encrypt)+'))')
print ("===========================================")
print ("Good! ,File Encrypted : "+str(myFile))
print ("===========================================")
print ("  Developed by Adel MD. | Umbrella Corp.")
print ("   be free to contact +967 733 477 848")
print ("            adeldawood@live.com")
print ("   Encrypted work_files TOOL beta:ver1.1")
print ("===========================================")
input ("      press ENTER to EXIT! Thanks")
#-----------------------------------------------------
