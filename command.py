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

input_dir_volmount=i_dir. ':' .i_dir
output_dir_volmount=o_dir. ':' .o_dir
bam_path=i_dir + "/" + bam
ref_path=i_dir + "/" + ref

# define command
def default_command(input_dir_volmount, output_dir_volmount, bam_path, ref_path, threads)
    command=[]
    command.append("docker")
    command.append("run")
    command.append("--ipc=host") # check if separate line --ipc=host
    command.append("-v")
    command.append(input_dir_volmount) 
    command.append("-v")
    command.append(output_dir_volmount) 
    command.append("kishwars/pepper_deepvariant:r0.4")
    command.append("run_pepper_margin_deepvariant call_variant")
    command.append("-b")
    command.append(bam_path)
    command.append("-f")
    command.append(ref_path)
    command.append("-t")
    command.append(threads)
    command.append("--ont")
    return command

#define truth vcf and bed
truth_vcf="HG002_GRCh38_1_22_v4.2.1_benchmark.vcf.gz"
truth_bed="HG002_GRCh38_1_22_v4.2.1_benchmark_noinconsistent.bed"

#path to truth vcf
truth_vcf_path= i_dir + "/" + truth_vcf
#path to output vcf
output_vcf_path= o_dir + "/" + o_vcf
#path to truth bed
truth_bed_path= i_dir + "/" + truth_bed

#define optional command hap.py
def optional_command(input_dir_mount, output_dir_mount, truth_vcf_path, output_vcf_path, truth_bed_path, ref_path, o_dir, threads)
    opt_command=[]
    opt_command.append("docker")
    opt_command.append("run")
    opt_command.append("-it") # check if separate line --ipc=host
    opt_command.append("-v")
    opt_command.append(input_dir_mount) 
    opt_command.append("-v")
    opt_command.append(output_dir_mount) 
    opt_command.append("jmcdani20/hap.py:v0.3.12")
    opt_command.append("/opt/hap.py/bin/hap.py")
    opt_command.append(truth_vcf_path)
    opt_command.append(output_vcf_path)
    opt_command.append("-f")
    opt_command.append(truth_bed_path)
    opt_command.append("-r")
    opt_command.append(ref_path)
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
    return opt_command

if args.with_margin:
    # subprocess.check_call(default_command, shell=True, executable='/bin/bash')
    # subprocess.check_call(opt_command, shell=True, executable='/bin/bash')
else:
    # subprocess.check_call(default_command, shell=True, executable='/bin/bash')
