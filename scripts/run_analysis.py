#!/usr/bin/env python3
"""
run_analysis.py
Simple pipeline for rabies virus genome analysis
"""

import os
import sys

def main():
    print("=" * 60)
    print("🧬 Rabies Genomic Surveillance Pipeline")
    print("📍 Samples from Sindh, Pakistan")
    print("=" * 60)

    # Your GenBank submissions
    accessions = ['PV491557', 'PV641711', 'PV641712', 'PV641713',
                  'PV641714', 'PV641715', 'PV641716', 'PV641717']
    
    print("\n📊 GenBank Submissions:")
    for acc in accessions:
        print(f"   - {acc}")
    
    print(f"\n📈 Total: {len(accessions)} whole genomes + 25 partial genes")
    print("\n✅ Pipeline ready!")
    
    print("\n" + "=" * 60)
    print("🚀 Next Steps:")
    print("   - Download reads from SRA")
    print("   - Assemble genomes with SPAdes")
    print("   - Build phylogenetic tree with IQ-TREE")
    print("=" * 60)

if __name__ == "__main__":
    main()
