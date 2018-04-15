class jobscheduler:
    def __init__(self,job_file):
        self.sum = 0
        self._read_jobs(job_file)
        self._schedule()
        self._compute_sum()

    def _read_jobs(self,job_file):
        with open(job_file,"r") as file:
            number_of_jobs = int(file.readline())
            self._jobs = [None] * number_of_jobs
            for index,line in enumerate(file):
                weight,length = line.split()
                self._jobs[index] = (int(weight),int(length))

    def _schedule(self):
        pass

    def _compute_sum(self):
        current_time = 0
        for job in self._jobs:
            current_time += job[1]
            self.sum += job[0] * current_time

class differencejobscheduler(jobscheduler):
        def _schedule(self):
            self._jobs = sorted(self._jobs,key = lambda job:(job[0] - job[1],job[0]),reverse=True)

class ratiojobscheduler(jobscheduler):
    def _schedule(self):
        self._jobs = sorted(self._jobs,key = lambda job:(job[0]/job[1]),reverse=True)

if __name__ == "__main__":
    diff_sched,ratio_sched = differencejobscheduler('week1/jobs.txt'),ratiojobscheduler('week1/jobs.txt')
    print(diff_sched.sum,ratio_sched.sum)
