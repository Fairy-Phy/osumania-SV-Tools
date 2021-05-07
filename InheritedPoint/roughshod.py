from Relium import calcurate, export, classes

start_offset = 71585
end_offset = 72385

max_scale = 10.0
min_scale = 0.01

min_step = 10
max_step = 1

beat = 4
sample_set = 2
sample_index = 0
volume = 100
effects = 0

## Main ##

# どうやらコンソールのパスからの指定らしい...
with open("./timingpoint.txt", mode='w') as exportfile:
	text: str = ""
	min_ok: bool = True
	i = start_offset
	while i <= end_offset:
		if min_ok:
			text += export.timingpoint(classes.TimingPoint(i, calcurate.inheritedpoint(min_scale), beat, sample_set, sample_index, volume, True, effects)) + "\n"
			min_ok = False
			i += min_step
		else:
			text += export.timingpoint(classes.TimingPoint(i, calcurate.inheritedpoint(max_scale), beat, sample_set, sample_index, volume, True, effects)) + "\n"
			min_ok = True
			i += max_step

	exportfile.write(text)
	pass
