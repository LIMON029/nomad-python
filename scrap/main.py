# -*- coding: utf-8 -*-
from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs

indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()
print(indeed_jobs)
print(so_jobs)