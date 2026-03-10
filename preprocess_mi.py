import run_cuda_MI
import cudf
import argparse

parser = argparse.ArgumentParser(
                    prog='Preprocess Matrix',
                    description='Eliminate zeroes to speed up MI calculation',
                    )
parser.add_argument('--input', '-i', type=str, required=True, help='Path to the input file')
parser.add_argument('--output', '-o', type=str, required=True, help='Path to the output file')
parser.add_argument('--separation', '-s', type=str, required=True, help='Type of separator in the input file (e.g., "," for CSV, "t" for TSV)')
parser.add_argument('--index_col', '-ic', type=int, default=0, help='Column to use as index (default is 0, which means the first column)')
parser.add_argument('--axis', '-a', type=int, choices=[0, 1], default=1, help='Axis to delete zeroes from (0 for rows, 1 for columns; default is 1)')
args = parser.parse_args()
fname = args.input
output_file = args.output
sep = args.separation
 # axis = 1 for columns as samples, axis = 0 for rows as samples; 
 # sep = type of separator in file
 # index_col = column to use as index (default is 0, which means the first column)

if sep == "t":
    sep = "\t"

### Delete zeroes from the input file and save the result to a new file
df = run_cuda_MI.delete_zeroes(fname, axis=args.axis, sep=sep, index_col=args.index_col)
df.to_csv(output_file, index=False)

### Run discretization and save the result to a new file (R_discretize.R)



