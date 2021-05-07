from Relium import calcurate, export, classes, convert
import math

start_offset = 122751
end_offset = 123024

start_scale = 3
max_scale = 0.0001

# 低いほどすぐ下がる
level = 1

beat = 4
sample_set = 1
sample_index = 1
volume = 60
effects = 0

## Main ##

# どうやらコンソールのパスからの指定らしい...
with open("./timingpoint.txt", mode='w') as exportfile:
	text: str = ""

	for i in range(start_offset, end_offset + 1):
		scale_multiple = (i - start_offset) / ((end_offset - start_offset) / 2)
		if scale_multiple > 1:
			scale_multiple = 2 - scale_multiple

		multipler = 1 - math.sqrt(1 - math.pow(scale_multiple, level))
		offset_scale = start_scale + multipler * (max_scale - start_scale)

		text += export.timingpoint(classes.TimingPoint(i, calcurate.inheritedpoint(offset_scale), beat, sample_set, sample_index, volume, True, effects)) + "\n"

		pass

	exportfile.write(text)
	pass
