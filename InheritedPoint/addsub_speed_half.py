from Relium import calcurate, export, classes
import math

"""
2次間数的にstart_scaleからmax_scaleまでをstart_offsetからend_offsetの間で行います
"""

start_offset = 34934
end_offset = 35479 - 1

start_scale = 0.01
end_scale = 1.2

# 低いほどすぐ下がる(上がる)
level = 2

beat = 4
sample_set = 1
sample_index = 0
volume = 60
effects = 0

## Main ##

# どうやらコンソールのパスからの指定らしい...
with open("./timingpoint1.txt", mode='w') as exportfile:
	text: str = ""

	for i in range(start_offset, end_offset + 1):
		scale_multiple = (i - start_offset) / (end_offset - start_offset)

		multipler = 1 - math.sqrt(1 - math.pow(scale_multiple, level))
		offset_scale = start_scale + multipler * (end_scale - start_scale)

		text += export.timingpoint(classes.TimingPoint(i, calcurate.inheritedpoint(offset_scale), beat, sample_set, sample_index, volume, True, effects)) + "\n"

		pass

	exportfile.write(text)
	pass
