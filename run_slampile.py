import os
import subprocess as sp

'''INPUTs'''
bam_filename = 'e.g. x.bam'
gtf_filename = 'e.g. hg38_transcriptome.gtf'
fa_filename =  'e.g. hg38.fa'



'''produce .bai'''
command = 'samtools index'+' '+bam_filename+' '+bam_filename + '.bai'
sp.call(command, shell=True)



'''run pileup'''
file = open('pileup_temp.R','w')
file1 = open('./blocks/pileup1.txt','r')
txt1 = file1.read()
txt1b = 'bamFile = ' + "'" + bam_filename + "'" + '\n'
file2 = open('./blocks/pileup2.txt','r')
txt2 = file2.read()
txt = txt1 + txt1b + txt2
file.write(txt)
file.close()

command = 'R --vanilla <pileup_temp.R'
sp.call(command, shell=True)
os.remove('pileup_temp.R')



'''run slampile'''
pileup_filename = bam_filename + '.pileup.csv'

file = open('slampile_temp.py','w')
file1 = open('./blocks/slampile1.txt','r')
txt1 = file1.read()
txt1b = 'gtf_filename = ' + "'"+gtf_filename+"'\n"
txt1c = 'fa_filename = ' + "'"+fa_filename+"'\n"
txt1d = 'pileup_filename = ' + "'"+pileup_filename+"'\n"
file2 = open('./blocks/slampile2.txt','r')
txt2 = file2.read()
txt = txt1 + txt1b + txt1c + txt1d + txt2
file.write(txt)
file.close()

command = 'python slampile_temp.py'
sp.call(command, shell=True)
os.remove('slampile_temp.py')
