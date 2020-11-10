# put your python code here
walk_in_hrs = int(input()) * 3600
walk_in_mins = int(input()) * 60
walk_in_secs = int(input())

run_in_hrs = int(input()) * 3600
run_in_mins = int(input()) * 60
run_in_secs = int(input())

first_total_time = walk_in_hrs + walk_in_mins + walk_in_secs
second_total_time = run_in_hrs + run_in_mins + run_in_secs

print(second_total_time - first_total_time)
