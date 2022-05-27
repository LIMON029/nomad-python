# -*- coding: utf-8 -*-
import csv


def save_to_file(jobs):
    # utf-8이 아닌 utf-8-sig를 사용하는 이유
    # utf-8는 BOM이 필요없어서 BOM이 있는 파일을 읽을 때 BOM을 파일 내용으로 처리
    # Excel은 csv파일을 읽을 때 BOM을 읽어 인코딩을 인식하지만 BOM이 없으면 유니코드로 읽는다
    with open('jobs.csv', mode="w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "link", "location"])
        for job in jobs:
            writer.writerow(list(job.values()))
    return
