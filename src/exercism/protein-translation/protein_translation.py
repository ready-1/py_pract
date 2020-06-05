def proteins(strand):
    codon_dict = {
        'AUG' : 'Methionine',
        'UUU' : 'Phenylalanine',
        'UUC' : 'Phenylalanine',
        'UUA' : 'Leucine',
        'UUG' : 'Leucine',
        'UCU' : 'Serine',
        'UCC' : 'Serine',
        'UCA' : 'Serine',
        'UCG' : 'Serine',
        'UAU' : 'Tyrosine',
        'UAC' : 'Tyrosine',
        'UGU' : 'Cysteine',
        'UGC' : 'Cysteine',
        'UGG' : 'Tryptophan',
        'UAA' : 'STOP',
        'UAG' : 'STOP',
        'UGA' : 'STOP'
        }

    protein_string = []
    # divide the strand into codons (3 char strings)
    for i in range(0, len(strand), 3):
        codon = strand[i:i + 3]
    # decode using dict
        prot = codon_dict[codon]
    # if STOP, break out of loop
        if prot == 'STOP':
            break
    # append onto protein_string
        protein_string.append(prot)
    return protein_string
