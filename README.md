# GRIPper2
Detect gene retrocopy insertion polymorphisms (GRIPs) from short-read paired-end WGS data

## Install:
Using conda (or mamba):
```
git clone https://github.com/adamewing/GRIPper2.git
cd GRIPper2
mamba env create -f gripper2.yml 
conda activate gripper2
pip install -e $PWD
```

Usage:
Currently the only command available is "call" (i.e. `gripper2 call`).

```
$ gripper2 call -h
usage: gripper2 call [-h] -r REF -b BAMS -g GTF [-p PROCS] [-m MASK] [--mindisc MINDISC] [--minjunc MINJUNC] [--remapscore REMAPSCORE] [--maxtsd MAXTSD] [--biotype BIOTYPE] [--exon_pairs]

optional arguments:
  -h, --help               show this help message and exit
  -r REF, --ref REF        reference genome (fasta)
  -b BAMS, --bams BAMS     .bam files (comma-delimited)
  -g GTF, --gtf GTF        .gtf file bgzipped/tabix indexed, generally expects ENSEMBL gtfs
  -p PROCS, --procs PROCS  parallel processes
  -m MASK, --mask MASK     mask insertion sites in regions (tabix indexed)
  --mindisc MINDISC        minimum discordant read count (default = 2)
  --minjunc MINJUNC        minimum split read count per junction (default = 1)
  --remapscore REMAPSCORE  minimum junction mapping to TE score (default = 0.5)
  --maxtsd MAXTSD          max TSD size (default = 100)
  --biotype BIOTYPE        restrict search to gtf/gff entries with given gene_biotype attribute (e.g. protein_coding)
  --exon_pairs             full exon pair output (default = output junction count)
```
