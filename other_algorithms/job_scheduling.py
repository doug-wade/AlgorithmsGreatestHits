import os

def get_weighted_completion_scores(job_list):
    """
    Gets the weighted completion score for a set of jobs by taking the sum of
    the total time elapsed at the end of each job * job weight.
    """
    total_length, score = 0, 0

    for job in job_list:
        total_length += job[1]
        score += (total_length * job[0])
    return score

def load_jobs(file_path):
    """
    Loads a list of jobs from a file with the following format:
    Line 1: an int, representing the number of jobs in the file_path
    The rest of the lines represent jobs in the format: job weight \s
    job length.  
    Returns a list of jobs as tuples in format (weight, length).
    """
    file_stream = open(file_path)
    num_jobs = file_stream.readline()
    jobs = []

    for i in range(int(num_jobs)):
        line = file_stream.readline()
        if line:
            job = line.split(' ')
            jobs.append((int(job[0]), int(job[1])))
    jobs.sort(key=lambda tup: -100 * (tup[0] / tup[1]) - (1/tup[1]))
    return(jobs)