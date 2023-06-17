import json
from statistics import stdev

from numpy import median, mean


input_file_path = "./dist/chumps.json"
output_file_path = "./dist/stats.json"


with open(input_file_path, 'r') as f:
  chumps = json.load(f)

status_proportions = (
    (-0.5,  'Recent loss to monty'),
    (-0.2,  'Not expecting bout soon'),
    (0.4,   'Bout due'),
    (0.7,   'Bout overdue!'),
    (99,    'BOUT WAAAAAY OVERDUE!!')

)

current_streak              = chumps[0]['streak']
current_chump               = chumps[0]
streak_median               = int(median([chump['streak'] for chump in chumps]))
streak_average              = int(mean([chump['streak'] for chump in chumps]))
streak_standard_deviation   = round(stdev([chump['streak'] for chump in chumps]), 2)
streak_max_chump            =  max(chumps, key=lambda chump:chump['streak'])

current_status_proportion   = ( current_streak - streak_median ) / streak_median
status                      = next((status for proportion, status in status_proportions if current_streak < proportion), None)

stats_result = {
    'current_streak':               current_streak,
    'status':                       status,
    'streak_average':               streak_average,
    'streak_standard_deviation':    streak_standard_deviation,
    'streak_median':                streak_median,
    'current_chump':                current_chump,
    'streak_max_chump':             streak_max_chump,
}


# print(f"{stats_result=}")
print(json.dumps(stats_result, indent=4))

with open(output_file_path, 'w') as f:
    json.dump(stats_result, f, indent=4)
