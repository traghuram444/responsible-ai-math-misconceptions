"""Only two label-free columns cross into the checker; no MAP model execution."""
from pathlib import Path
import pandas as pd
from map_misconceptions.e019_checker import normalize, sha, write_new

ROOT = Path(__file__).resolve().parents[1]
if __name__ == '__main__':
    data = ROOT / 'data/raw/train.csv'
    if sha(data) != '0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c':
        raise ValueError('Data identity changed.')
    frame = pd.read_csv(data, usecols=['QuestionText','MC_Answer'], dtype=str, keep_default_na=False)
    pairs = sorted(set((normalize(q),normalize(a)) for q,a in zip(frame.QuestionText,frame.MC_Answer)))
    destination = ROOT / 'artifacts/e019_setup/catalogue.json'
    write_new(destination, [{'question':q, 'proposed_answer':a} for q,a in pairs])
    write_new(destination.with_name('catalogue_receipt.json'), {'rows':len(frame), 'pairs':len(pairs),
        'catalogue_sha256':sha(destination), 'columns':['QuestionText','MC_Answer']})
    print(f'Label-free preparation complete: {len(frame)} rows; {len(pairs)} distinct pairs. No labels read.')
