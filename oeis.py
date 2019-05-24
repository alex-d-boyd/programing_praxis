#! /usr/bin/env python3

import sys

import requests

OEIS_URL = 'https://oeis.org/search'

def get_seq(seq_name):
    """Fetch and return an OEIS sequence in JSON format"""
    params = {
        'q': f'id:{seq_name}',
        'fmt': 'json',
        }
    response = requests.get(OEIS_URL, params)
    response.raise_for_status()
    return response.json()

def extract_seq(seq_json):
    """Extract and return the sequences from OEIS JSON data"""
    results = seq_json['results']
    seqs = dict()
    for result in results:
        number = result['number']
        a_id = f'A{number:06}'
        seqs[a_id] = result['data']
    if seqs:
        return seqs
    else:
        return None

if __name__ == '__main__':
    seq_id = sys.argv[1]
    seq_json = get_seq(seq_id)
    seq_data = extract_seq(seq_json)
    if seq_data is not None:
        for seq in seq_data:
            print(f'{seq}: {seq_data[seq]}')
    else:
        print('No sequence found')
