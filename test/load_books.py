import os
import subprocess
import thread

book_dir="/home/chongyangchen/pypro/crawl/test/book/"
pdf_dir ="/home/chongyangchen/pypro/crawl/test/pdf/"
cmds = "ls %s" % pdf_dir
threads = []

def print_file(filename, i):
    filename1 = "%s%s" % (pdf_dir, filename)
    with open(filename1) as fi:
        for line in fi:
            if "http" in line:
                fo.write(line) 
    fo.close
    fi.close
def make_dir(dirname):
    b_dir = "%s%s"%(book_dir,dirname)
    print b_dir

tmp = subprocess.check_output(
    cmds,
    stderr=subprocess.STDOUT,
    shell=True)
for t in tmp.split():
    if "txt" in t:
        filename = "%s"%t
        #print filename
        try:
           #create some threads
           threads.append(thread.start_new_thread( make_dir, (filename,) ))
        except:
           print "Error: unable to start thread"

for t in threads:
    t.join()
 
