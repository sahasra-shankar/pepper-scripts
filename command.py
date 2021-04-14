import argparse
import subprocess

###### FOR PEPPER-ONT #####
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
# User specified output VCF
parser.add_argument('-V', '--output_vcf')
# User specified thread number or default=64
parser.add_argument('-T', '--thread_num', default='64')

## Running with optional -> hap.py
parser.add_argument('-WM', '--with_margin')

args=parser.parse_args()
i_dir=args.input_dir
o_dir=args.output_dir
bam=args.bam_file
ref=args.ref_file
o_pre=args.output_prefix
o_vcf=args.output_vcf
threads=args.thread_num

# define command
command=[]
command.append("docker")
command.append("run")
command.append("--ipc=host") # check if separate line --ipc=host
command.append("-v")
command.append(i_dir) # verify: 1 val or 2(input:/input)-> add line append (":")
command.append("-v")
command.append(o_dir) # verify: 1 val or 2(input:/input)
command.append("kishwars/pepper_deepvariant:r0.4")
command.append("run_pepper_margin_deepvariant call_variant")
command.append("-b")
command.append(i_dir)
command.append("/")
command.append(bam) # check if add line append ("/") needed
command.append("-f")
command.append(i_dir)
command.append("/")
command.append(bam)
command.append("-t")
command.append(threads)
command.append("--ont")

# subprocess.check_call(command, shell=True, executable='/bin/bash')

#define truth vcf and bed
truth_vcf="HG002_GRCh38_1_22_v4.2.1_benchmark.vcf.gz"
truth_bed="HG002_GRCh38_1_22_v4.2.1_benchmark_noinconsistent.bed"

#define optional command hap.py
opt_command=[]
opt_command.append("docker")
opt_command.append("run")
opt_command.append("-it") # check if separate line --ipc=host
opt_command.append("-v")
opt_command.append(i_dir) # verify: 1 val or 2(input:/input)-> add line append (":")
opt_command.append("-v")
opt_command.append(o_dir) # verify: 1 val or 2(input:/input)
opt_command.append("jmcdani20/hap.py:v0.3.12")
opt_command.append("/opt/hap.py/bin/hap.py")
opt_command.append(i_dir)
opt_command.append(truth_vcf)
opt_command.append(o_dir)
opt_command.append(o_vcf)

opt_command.append("-f")
opt_command.append(i_dir)
opt_command.append("/")
opt_command.append(truth_bed)
opt_command.append("-r")
opt_command.append(i_dir)
opt_command.append("/")
opt_command.append(ref)
opt_command.append("-o")
opt_command.append(o_dir)
opt_command.append("/happy.output")
opt_command.append("--pass-only")
opt_command.append("-l")
opt_command.append("chr20") # quotes or no quotes
opt_command.append("--engine")
# opt_command.append("=")
opt_command.append("vcfeval") # quotes or no quotes
opt_command.append("--threads")
# opt_command.append("=")
opt_command.append(threads)

if args.with_margin:
    # subprocess.check_call(opt_command, shell=True, executable='/bin/bash')
