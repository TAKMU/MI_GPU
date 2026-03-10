import run_cuda_MI
import cudf
import argparse

parser = argparse.ArgumentParser(
                    prog='Preprocess Matrix',
                    description='Eliminate zeroes to speed up MI calculation',
                    )
parser.add_argument('--input', '-i', type=str, required=True, help='Path to the input file')
parser.add_argument('--output', '-o', type=str, required=True, help='Path to the output file')
args = parser.parse_args()
fname = args.input
output_file = args.output
 # axis = 1 for columns as samples, axis = 0 for rows as samples; 
 # sep = type of separator in file
 # index_col = column to use as index (default is 0, which means the first column)

### Delete zeroes from the input file and save the result to a new file
df = run_cuda_MI.delete_zeroes(fname, axis=1, sep="\t", index_col=0)
df.to_csv(output_file, index=False)

### Run discretization and save the result to a new file (R_discretize.R)



