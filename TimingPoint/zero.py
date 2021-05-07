from Relium import calcurate, classes, parser, constant

# 作成中(調整中)

source_file = r""

target_start_offset = 92479
target_end_offset = 96570

avgbpm = 220

beat = 4
sample_set = 1
sample_index = 0
volume = 60
effects = 0

End_kiai = False

## Main ##

parsed_map = parser.parsefile(source_file)

target_hitobjects = [output for output in parsed_map.HitObjects if output.offset >= target_start_offset and output.offset <= target_end_offset]

last_process_offset = 0
result_object = classes.ParsedBeatmap([], [])
for target_hitobject in target_hitobjects:
	if target_hitobject.offset == last_process_offset: continue
	if target_hitobject.offset == target_start_offset:
		result_object.TimingPoints.append(classes.TimingPoint(target_start_offset, constant.zero_bpm, beat, sample_set, sample_index, volume, False, effects))
	elif target_hitobject.offset == target_end_offset:
		result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset, calcurate.timingpoint(avgbpm), beat, sample_set, sample_index, volume, False, effects))
	else:
		result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset, constant.inf_bpm, beat, sample_set, sample_index, volume, False, effects))
		result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset + 1, constant.zero_bpm, beat, sample_set, sample_index, volume, False, effects))
	last_process_offset = target_hitobject.offset

# どうやらコンソールのパスからの指定らしい...
parser.parsesave(result_object, "export.txt")
