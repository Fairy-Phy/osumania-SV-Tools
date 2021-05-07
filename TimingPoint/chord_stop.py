from Relium import calcurate, classes, parser, constant

source_file = r""

target_start_offset = 125342
target_end_offset = 125479

avgbpm = 220

increase = 75

beat = 4
sample_set = 1
sample_index = 0
volume = 60
effects = 0

End_kiai = False

# 0 => start zero, for end. 1 => from start, end undo
mode = 1

## Main ##

parsed_map = parser.parsefile(source_file)

target_hitobjects = [output for output in parsed_map.HitObjects if output.offset >= target_start_offset and output.offset <= target_end_offset]

last_process_offset = 0
result_object = classes.ParsedBeatmap([], [])
for target_hitobject in target_hitobjects:
	if target_hitobject.offset == last_process_offset: continue

	if mode == 0:
		if target_hitobject.offset == target_start_offset:
			result_object.TimingPoints.append(classes.TimingPoint(target_start_offset, constant.zero_bpm, beat, sample_set, sample_index, volume, False, effects))
		elif target_hitobject.offset == target_end_offset:
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset - 1, calcurate.timingpoint(avgbpm * increase), beat, sample_set, sample_index, volume, False, effects))
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset, calcurate.timingpoint(avgbpm), beat, sample_set, sample_index, volume, False, effects - 1 if End_kiai else effects))
		else:
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset - 1, calcurate.timingpoint(avgbpm * increase), beat, sample_set, sample_index, volume, False, effects))
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset, constant.zero_bpm, beat, sample_set, sample_index, volume, False, effects))
	elif mode == 1:
		if target_hitobject.offset == target_start_offset:
			result_object.TimingPoints.append(classes.TimingPoint(target_start_offset, calcurate.timingpoint(avgbpm * increase), beat, sample_set, sample_index, volume, False, effects))
			result_object.TimingPoints.append(classes.TimingPoint(target_start_offset + 1, constant.zero_bpm, beat, sample_set, sample_index, volume, False, effects))
		elif target_hitobject.offset == target_end_offset:
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset, calcurate.timingpoint(avgbpm), beat, sample_set, sample_index, volume, False, effects - 1 if End_kiai else effects))
		else:
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset, calcurate.timingpoint(avgbpm * increase), beat, sample_set, sample_index, volume, False, effects))
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset + 1, constant.zero_bpm, beat, sample_set, sample_index, volume, False, effects))

	last_process_offset = target_hitobject.offset

# どうやらコンソールのパスからの指定らしい...
parser.parsesave(result_object, "export.txt")
