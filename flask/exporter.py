# -*- coding: utf-8 -*-
import csv


def save_to_file(jobs, word):
    with open(f'{word} Jobs.csv', mode="w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "company", "link", "location"])
        for job in jobs:
            writer.writerow(list(job.values()))
    return
