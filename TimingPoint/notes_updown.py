from Relium import calcurate, classes, parser, constant

source_file = r""

target_start_offset = 105570
target_end_offset = 109115

avgbpm = 220

max_laneheight = 370

beat = 4
sample_set = 1
sample_index = 0
volume = 60
effects = 0

# 0 => up, 1 => down
mode = 0

## Main ##

parsed_map = parser.parsefile(source_file)

target_hitobjects = [output for output in parsed_map.HitObjects if output.offset >= target_start_offset and output.offset <= target_end_offset]

last_process_offset = 0
result_object = classes.ParsedBeatmap([], [])
for target_hitobject in target_hitobjects:
	if target_hitobject.offset == last_process_offset:
		target_hitobjects.remove(target_hitobject)

	last_process_offset = target_hitobject.offset

increase = max_laneheight / len(target_hitobjects)
for target_hitobject_i in range(len(target_hitobjects)):
	target_hitobject = target_hitobjects[target_hitobject_i]

	if mode == 0:
		if target_hitobject_i == 0:
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset, constant.inf_bpm, beat, sample_set, sample_index, volume, False, effects))
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset + 1, constant.zero_bpm, beat, sample_set, sample_index, volume, False, effects))
		elif target_hitobject_i == len(target_hitobjects) - 1:
			if target_hitobject_i == 0:
				result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset - 1, constant.zero_bpm, beat, sample_set, sample_index, volume, False, effects))
			else:
				result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset - 1, calcurate.line_notesposition(avgbpm, increase * target_hitobject_i), beat, sample_set, sample_index, volume, False, effects))
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset, calcurate.timingpoint(avgbpm), beat, sample_set, sample_index, volume, False, effects))
		else:
			if target_hitobject_i == 0:
				result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset - 1, constant.zero_bpm, beat, sample_set, sample_index, volume, False, effects))
			else:
				result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset - 1, calcurate.line_notesposition(avgbpm, increase * target_hitobject_i), beat, sample_set, sample_index, volume, False, effects))
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset, constant.inf_bpm, beat, sample_set, sample_index, volume, False, effects))
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset + 1, constant.zero_bpm, beat, sample_set, sample_index, volume, False, effects))
	elif mode == 1:
		if target_hitobject_i == 0:
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset, constant.inf_bpm, beat, sample_set, sample_index, volume, False, effects))
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset + 1, constant.zero_bpm, beat, sample_set, sample_index, volume, False, effects))
		elif target_hitobject_i == len(target_hitobjects) - 1:
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset - 1, calcurate.line_notesposition(avgbpm, increase * (len(target_hitobjects) - target_hitobject_i)), beat, sample_set, sample_index, volume, False, effects))
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset, calcurate.timingpoint(avgbpm), beat, sample_set, sample_index, volume, False, effects))
		else:
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset - 1, calcurate.line_notesposition(avgbpm, increase * (len(target_hitobjects) - target_hitobject_i)), beat, sample_set, sample_index, volume, False, effects))
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset, constant.inf_bpm, beat, sample_set, sample_index, volume, False, effects))
			result_object.TimingPoints.append(classes.TimingPoint(target_hitobject.offset + 1, constant.zero_bpm, beat, sample_set, sample_index, volume, False, effects))
	else: print("mode not found")

# どうやらコンソールのパスからの指定らしい...
parser.parsesave(result_object, "export.txt")
