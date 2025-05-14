#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

# setting up the argument fixed
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA and search for a motif')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# display help when there is no argument provided
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# parsing the arguments
args = parser.parse_args()
args.seq = args.seq.upper() #added to deal well with lower-case sequences

# Sequence Classification as DNA or RNA
if re.search('^[ACGTU]+$', args.seq):  # A, C, G, T, U nucleotides will be used
    # Detect invalid sequence 
    if 'T' in args.seq and 'U' in args.seq:
        print("Contains both T (DNA) and U (RNA).")
    
    # DNA sequence (contains T but not U)
    elif 'T' in args.seq:
        print('The sequence is DNA.')
    
    # RNA sequence (contains U but not T)
    elif 'U' in args.seq:
        print('The sequence is RNA.')
    
    # Sequence without T or U can be DNA or RNA
    else:
        print('The sequence can be DNA or RNA.')
else:
    # any other letter than above
    print('The sequence is not DNA nor RNA.')
    sys.exit(1) # not to search for a motif with other letters


# Motif Search if/when provided
  if args.motif:
    args.motif = args.motif.upper()  # Convert motif to uppercasey
    if args.motif in args.seq:
        position = args.seq.find(args.motif) + 1
        print(f"Motif '{args.motif}' was found at position {position}.")
    else:
        print(f"Motif '{args.motif}' is not found in the sequence.")
