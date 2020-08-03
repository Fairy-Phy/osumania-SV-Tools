from osumania_svtools import calcurate, classes, parser, constant

# 作成中(調整中)

source_file = r"D:\\osu!_mania\\Songs\\beatmap-637318725988657140-Kairiki Bear+Crusher - Electrostatic Human (Crusher Remix) ft. Hatsune Miku English\\Kairiki Bear+Crusher ft. Hatsune Miku - Electrostatic Human (Crusher Remix) ([Fairy]Phy) [Jack+SV].osu"

target_start_offset = 57227
target_end_offset = 73923

avgbpm = 115

increase = 110

beat = 4
sample_set = 1
sample_index = 1
volume = 100
effects = 1

End_kiai = True

mode = 1

## Main ##

parsed_map = parser.parsefile(source_file)

target_hitobjects = [output for output in parsed_map.HitObjects if output.offset >=
					 target_start_offset and output.offset <= target_end_offset]

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
