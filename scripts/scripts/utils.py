"""
utils.py
Utility functions for rabies genomic analysis
"""

def parse_fasta(file_path):
    """Read FASTA file and return sequences"""
    sequences = {}
    with open(file_path, 'r') as f:
        lines = f.readlines()
        current_id = None
        seq = []
        for line in lines:
            line = line.strip()
            if line.startswith('>'):
                if current_id:
                    sequences[current_id] = ''.join(seq)
                current_id = line[1:]
                seq = []
            else:
                seq.append(line)
        if current_id:
            sequences[current_id] = ''.join(seq)
    return sequences

def validate_accession(accession):
    """Validate GenBank accession format"""
    # Basic validation for rabies GenBank accessions
    return accession.startswith('PV') and len(accession) >= 6

def get_sample_info(accession):
    """Get sample information for a given accession"""
    # Example - replace with your actual data
    info = {
        'PV491557': {'host': 'Dog', 'location': 'Sindh', 'year': 2024},
        'PV641711': {'host': 'Dog', 'location': 'Sindh', 'year': 2025},
        # Add more as needed
    }
    return info.get(accession, {'host': 'Unknown', 'location': 'Unknown', 'year': 'Unknown'})
