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

Output:
Tab-delimited, column descriptions:

|--------------------|---------------------------------------------------------------------------------------------------------------|
|Chrom               |Chromosome                                                                                                     |
|Left_Break          |Leftmost breakpoint                                                                                            |
|Right_Break         |Rightmost breakpoint                                                                                           |
|Ins_Strand          |Strand of insertion, relative to reference gene (+ = same orientation as ref, - = opposite orientation to ref) |
|Gene_Name           |Donor gene name                                                                                                |
|Gene_Chrom          |Chromosome of donor gene                                                                                       |
|Gene_Start          |Leftmost position of breakpoint in donor gene                                                                  |
|Gene_End            |Rightmost position of breakpoints in donor gene                                                                |
|Gene_Strand         |Strand of donor gene from annotation                                                                           |
|Sample_Count        |Number of samples in which GRIP is detected                                                                    |
|Sample_List         |Samples in which GRIP is detected                                                                              |
|Exons_Overlapped    |Number of exons between Gene_Start and Gene_End                                                                |
|Left_Map_Score      |Mapping score of left end vs genome                                                                            |
|Right_Map_Score     |Mapping score of right end vs genome                                                                           |
|Left_Split_Support  |Number of split reads supporting left breakpoint                                                               |
|Left_Split_Samples  |Number of split reads supporting left breakpoint per sample                                                    |
|Right_Split_Support |Number of split reads supporting right breakpoint                                                              |
|Right_Split_Samples |Number of split reads supporting right breakpoint per sample                                                   |
|Disc_Read_Count     |Number of supporting discordant reads                                                                          |
|Disc_Samples        |Number of supporting discordant reads per sample                                                               |
|Left_Split_Len      |Length (bp) of non-reference part of left consensus (lower-case bases)                                         |
|Right_Split_Len     |Length (bp) of non-reference part of right consensus (lower-case bases)                                        |
|Left_Cons           |Left consensus                                                                                                 |
|Right_Cons          |Right consensus                                                                                                |
|TSD                 |Target site duplication (NA if not present)                                                                    |
|Exon_Pairs          |Number of potential exon-exon joins detected or list of exon-exon pairs (if --exon_pairs is given)             |

