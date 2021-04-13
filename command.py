import subprocess
import argparse

## ARGUMENT PARSER(user specifies input and outpur dir, threads, output prefix, BAM and REF)
parser=argparse.ArgumentParser()

# User specified input directory
parser.add_argument('')
# User specified output directory

# User specified BAM

# User specified REF

# User specified output prefix

command="pwd"

subprocess.check_call(command, shell=True, executable='/bin/bash')
