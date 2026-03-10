import argparse
import cudf
import cupy as cp
from run_cuda_MI import simplify_labels, create_mi_matrix
import pandas as pd
parser = argparse.ArgumentParser(
                    prog='Create MI Matrix',
                    description='Create a Mutual Information matrix',
                    )
parser.add_argument('--input', '-i', type=str, required=True, help='Path to the input file')
parser.add_argument('--output', '-o', type=str, required=True, help='Path to the output file')
args = parser.parse_args()
fname = args.input
output_file = args.output

print("Starting MI matrix generation...")
df = simplify_labels(fname)
mi_matrix = create_mi_matrix(df)
mi_matrix.to_csv(output_file)

