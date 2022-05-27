# -*- coding: utf-8 -*-
from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file

so_jobs = get_so_jobs()
indeed_jobs = get_indeed_jobs()

jobs = so_jobs + indeed_jobs

# CSV: Comma Separated Values
save_to_file(jobs)
