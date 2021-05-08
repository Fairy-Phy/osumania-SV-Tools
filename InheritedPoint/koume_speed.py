from Relium import calcurate, export, classes, parser
from typing import List
import math

"""
緑線でノーツ間を均等にします
正直タイミングがつかめないのでプレイする側は最悪です
"""

source_file = r""
aveBPM = 170

beat = 4
sample_set = 1
sample_index = 0
volume = 100
effects = 0

## Main ##

parsed_file = parser.parsefile(source_file)
process_timingpoint = list()
for timingpoint_i in range(len(parsed_file.TimingPoints)):
	timingpoint = parsed_file.TimingPoints[timingpoint_i]
	process_timingpoint.append(timingpoint)
	if timingpoint.inherited: continue

	target_hitobjects: List[classes.HitObject]

	next_timingpoint_i = 1
	next_timingpoint = None
	while timingpoint_i + next_timingpoint_i != len(parsed_file.TimingPoints):
		test_timingpoint = parsed_file.TimingPoints[timingpoint_i + next_timingpoint_i]
		if test_timingpoint.inherited:
			next_timingpoint_i += 1
		else:
			next_timingpoint = test_timingpoint
			break
		pass
	if next_timingpoint == None:
		target_hitobjects = [output for output in parsed_file.HitObjects if output.offset >= timingpoint.offset]
	else:
		target_hitobjects = [output for output in parsed_file.HitObjects if output.offset >= timingpoint.offset and output.offset <= next_timingpoint.offset]

	last_hitobject_offset = 0
	for check_hitobject in target_hitobjects.copy():
		if (last_hitobject_offset == check_hitobject.offset):
			target_hitobjects.remove(check_hitobject)
		last_hitobject_offset = check_hitobject.offset

	timingPoint_BPM = round(calcurate.timingpoint(timingpoint.beat_length))
	equal_scale = aveBPM / timingPoint_BPM

	for hitobject_i in range(len(target_hitobjects)):
		hitobject: classes.HitObject = target_hitobjects[hitobject_i]
		if hitobject_i + 1 != len(target_hitobjects):
			next_hitobject: classes.HitObject = target_hitobjects[hitobject_i + 1]
			def detail_offset(before_hitobject_offset):
				for beatsnap in [16, 12]:
					BPM_timingpoint = calcurate.timingpoint(timingPoint_BPM)
					beatsnap_timingpoint = BPM_timingpoint / beatsnap
					for beatsnap_multi in range(beatsnap + 1):
						answer_offset = timingpoint.offset + (beatsnap_timingpoint * beatsnap_multi)
						if math.floor(answer_offset) == before_hitobject_offset:
							return answer_offset
						pass
					pass
				return before_hitobject_offset
			next_hitobject_offset = detail_offset(next_hitobject.offset)
			hitobject_offset = detail_offset(hitobject.offset)
			answer_scale = round(equal_scale / (next_hitobject_offset - hitobject_offset) * (calcurate.timingpoint(timingPoint_BPM) / 4), 2)
			print(hitobject.offset, answer_scale)
			process_timingpoint.append(classes.TimingPoint(hitobject.offset, calcurate.inheritedpoint(answer_scale), beat, sample_set, sample_index, volume, True, effects))
	pass

process_parsed = classes.ParsedBeatmap(process_timingpoint, parsed_file.HitObjects)
# どうやらコンソールのパスからの指定らしい...
parser.parsesave(process_parsed, "./inheritedpoint.txt")
