from pathlib import Path

import pandas as pd


def transform():
    project_path = Path(__file__).parents[1].resolve()

    raw_path = project_path / 'data/raw/BAH1002_-_Open_Requisitions_Report_(ORR) (1).xlsx'
    jobs = pd.read_excel(raw_path.resolve())

    ds_jobs = jobs[jobs['Job Posting'].str.contains('Data Scientist')]['Job Profile Skills']

    ds_skills = ds_jobs.str.split('\n\n')

    ds_flat = ds_skills.explode()

    ds_count = ds_flat.value_counts().reset_index()

    save_path = project_path / 'data/processed/ds_skills.csv'
    ds_count.to_csv(save_path.resolve(), index=False)


if __name__ == '__main__':
    transform()
