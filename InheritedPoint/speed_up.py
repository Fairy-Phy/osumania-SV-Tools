from Relium import calcurate, export, classes

start_offset = 144570
end_offset = 153297 - 1

start_scale = 0.5
end_scale = 1.0

beat = 4
sample_set = 1
sample_index = 0
volume = 60
effects = 0

## Main ##

# どうやらコンソールのパスからの指定らしい...
with open("./timingpoint.txt", mode='w') as exportfile:
	offset_scale: float = (end_scale - start_scale) / (end_offset - start_offset)

	text: str = ""
	for i in range(start_offset, end_offset + 1):
		if i == end_offset:
			text += export.timingpoint(classes.TimingPoint(i, calcurate.inheritedpoint(end_scale), beat, sample_set, sample_index, volume, True, effects)) + "\n"
		else:
			text += export.timingpoint(classes.TimingPoint(i, calcurate.inheritedpoint((offset_scale * (i - start_offset)) + start_scale), beat, sample_set, sample_index, volume, True, effects)) + "\n"

	exportfile.write(text)
	pass
