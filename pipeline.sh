#!/bin/bash
var_path=$PWD  
python preprocess_mi.py --input data/example.tsv --output data/simplified.csv --separation "t" --axis 1
Rscript R_discretize.R --input data/simplified.csv --output data/discretized.csv --working_dir $var_path
python generate_matrix.py --input data/discretized.csv --output data/mi_matrix.csv