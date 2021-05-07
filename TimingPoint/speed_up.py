from Relium import calcurate, export, classes

start_offset = 3581
end_offset = 13958

start_bpm = 200
end_bpm = 2021
interval = 1

beat = 4
sample_set = 1
sample_index = 0
volume = 100
effects = 0

## Main ##

# どうやらコンソールのパスからの指定らしい...
with open("./timingpoint.txt", mode='w') as exportfile:
	offset_bpm: float = (end_bpm - start_bpm) / (end_offset - start_offset)

	text: str = ""
	for i in range(start_offset, end_offset + 1, interval):
		if i == end_offset:
			text += export.timingpoint(classes.TimingPoint(i, calcurate.timingpoint(end_bpm), beat, sample_set, sample_index, volume, False, effects)) + "\n"
		else:
			text += export.timingpoint(classes.TimingPoint(i, calcurate.timingpoint((offset_bpm * (i - start_offset)) + start_bpm), beat, sample_set, sample_index, volume, False, effects)) + "\n"

	exportfile.write(text)
	pass
