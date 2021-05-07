from Relium import calcurate, classes, export

start_offset = 100933
end_offset = 101068

bpm = 220
scale = 10.0

space = 2

beat = 4
sample_set = 1
sample_index = 0
volume = 60
effects = 0

## Main ##

bpmscale = bpm * scale

# どうやらコンソールのパスからの指定らしい...
with open("./timingpoint.txt", mode='w') as exportfile:
	text: str = ""
	i = start_offset
	while i <= end_offset:
		text += export.timingpoint(classes.TimingPoint(i, calcurate.timingpoint(bpmscale), beat, sample_set, sample_index, volume, False, effects)) + "\n"
		i += space

	exportfile.write(text)
	pass
