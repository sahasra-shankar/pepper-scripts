import subprocess
import argparse

## ARGUMENT PARSER(user specifies input and outpur dir, threads, output prefix, BAM and REF)
parser=argparse.ArgumentParser()

# User specified input directory
parser.add_argument('-I', '--input_dir')
# User specified output directory
parser.add_argument('-O', '--output_dir')
# User specified BAM
parser.add_argument('-B', '--bam_file')
# User specified REF
parser.add_argument('-R', '--ref_file')
# User specified output prefix
parser.add_argument('-P', '--output_prefix')

# command="pwd"
# subprocess.check_call(command, shell=True, executable='/bin/bash')
