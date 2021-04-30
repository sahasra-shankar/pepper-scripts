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
margin=args.with_margin

# for default command
bam_path=i_dir + "/" + bam
ref_path=i_dir + "/" + ref

# for optional command
#define truth vcf and bed
truth_vcf="HG002_GRCh38_1_22_v4.2.1_benchmark.vcf.gz"
truth_bed="HG002_GRCh38_1_22_v4.2.1_benchmark_noinconsistent.bed"

#path to truth vcf
truth_vcf_path= i_dir + "/" + truth_vcf
#path to output vcf
output_vcf_path= o_dir + "/" + o_vcf
#path to truth bed
truth_bed_path= i_dir + "/" + truth_bed



class Command:
    def __init__(self, i_dir, o_dir, bam_path, ref_path, o_pre, threads, truth_vcf_path, output_vcf_path, truth_bed_path):
        self.i_dir=i_dir
        self.o_dir=o_dir
        self.bam_path=bam_path
        self.ref_path=ref_path
        self.o_pre=o_pre
        self.threads=threads
        self.truth_vcf_path=truth_vcf_path
        self.output_vcf_path=output_vcf_path
        self.truth_bed_path=truth_bed_path

    def build_defcommand(self):
        def_command="docker run --ipc=host"
        add_i_volmount="-v " + self.i_dir + ":" + self.i_dir
        add_o_volmount="-v " + self.o_dir + ":" + self.o_dir 
        add_prog_run="kishwars/pepper_deepvariant:r0.4 run_pepper_margin_deepvariant call_variant"
        add_bam_path="-b " + self.bam_path
        add_ref_path="-f " + self.ref_path
        add_output="-o " + self.o_dir
        add_out_pre="-p " + self.o_pre
        add_threads="-t " + self.threads
        add_seq_type="--ont"
        full_def_com="{} {} {} {} {} {} {} {}".format(def_command, add_i_volmount, add_o_volmount, add_prog_run, add_bam_path, add_ref_path, add_output, add_out_pre, add_threads, add_seq_type)
        return full_def_com

    #def run_command(self):

if args.with_margin:
    ont_command=Command(i_dir, o_dir, bam_path, ref_path, o_pre, threads, truth_vcf_path, output_vcf_path, truth_bed_path)
    print(ont_command.build_defcommand())
    # subprocess.check_call(default_command, shell=True, executable='/bin/bash')
    # subprocess.check_call(opt_command, shell=True, executable='/bin/bash')
else:
    ont_command=Command(i_dir, o_dir, bam_path, ref_path, o_pre, threads, truth_vcf_path, output_vcf_path, truth_bed_path)
    print(ont_command.build_defcommand())
    # subprocess.check_call(default_command, shell=True, executable='/bin/bash')




    
