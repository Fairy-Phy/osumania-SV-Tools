from Relium import calcurate, classes, parser, constant, convert

source_file = r""

target_start_offset = 2500
target_end_offset = 4000

avgbpm = 60

beat = 4
sample_set = 1
sample_index = 1
volume = 100
effects = 0

## Main ##

parsed_map = parser.parsefile(source_file)

target_hitobjects = [output for output in parsed_map.HitObjects if output.offset >= target_start_offset and output.offset <= target_end_offset]

i = int(target_start_offset)
result_object = classes.ParsedBeatmap([], [])
while (i <= target_end_offset):
	result_object.TimingPoints.append(classes.TimingPoint(i, 0.2, beat, sample_set, sample_index, volume, False, effects))
	i += 1

	if i == target_end_offset:
		result_object.TimingPoints.append(classes.TimingPoint(i, calcurate.timingpoint(avgbpm), beat, sample_set, sample_index, volume, False, effects))
		break

	zero_break = False
	for count_ in range(6):
		result_object.TimingPoints.append(classes.TimingPoint(i, constant.zero_bpm, beat, sample_set, sample_index, volume, False, effects))
		i += 1
		if i == target_end_offset:
			result_object.TimingPoints.append(classes.TimingPoint(i, calcurate.timingpoint(avgbpm), beat, sample_set, sample_index, volume, False, effects))
			zero_break = True
			break
	if zero_break: break

	last_note_offset = 0
	ms_control = 0
	for hitobject in reversed([output for output in target_hitobjects if output.offset >= target_start_offset and output.offset <= i]):
		if last_note_offset != hitobject.offset:
			note_ms = i - hitobject.offset
			# print("note_ms - ms_control:", note_ms - ms_control)
			if note_ms - ms_control > 800: break

			try:
				result_object.TimingPoints.append(classes.TimingPoint(i, calcurate.line_notesposition(avgbpm, note_ms - ms_control), beat, sample_set, sample_index, volume, False, effects))
			except ZeroDivisionError:
				result_object.TimingPoints.append(classes.TimingPoint(i, constant.zero_bpm, beat, sample_set, sample_index, volume, False, effects))

			i += 1
			if i == target_end_offset:
				result_object.TimingPoints.append(classes.TimingPoint(i, calcurate.timingpoint(avgbpm), beat, sample_set, sample_index, volume, False, effects))
				break

			ms_control += (note_ms - ms_control)
			# print("ms_control:", ms_control)

		if i == hitobject.offset: continue
		result_object.HitObjects.append(convert.voidobject(hitobject.key_position, i))
		
		last_note_offset = hitobject.offset
	else:
		continue
	break

# どうやらコンソールのパスからの指定らしい...
parser.parsesave(result_object, "export.txt")
