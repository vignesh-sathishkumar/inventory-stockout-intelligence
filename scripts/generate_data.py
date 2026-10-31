"""Regenerate the deterministic synthetic CSVs and dashboard metrics.
Run from repository root: python scripts/generate_data.py
The source generator is included in scripts/build_dataset.py.
"""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('build_dataset.py')),run_name='__main__')
