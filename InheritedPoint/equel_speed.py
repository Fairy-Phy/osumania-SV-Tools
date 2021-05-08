from Relium import calcurate, export, classes, parser

"""
バラバラなBPMをaveBPMを基準に速度を均等にします
"""

source_file = r""
aveBPM = 145

beat = 4
sample_set = 1
sample_index = 0
volume = 100
effects = 0

## Main ##

parsed_file = parser.parsefile(source_file)
process_timingpoint = list()
for timingpoint in parsed_file.TimingPoints:
	process_timingpoint.append(timingpoint)

	if timingpoint.inherited: continue
	timingPoint_BPM = round(calcurate.timingpoint(timingpoint.beat_length))
	equal_scale = aveBPM / timingPoint_BPM
	if calcurate.inheritedpoint(equal_scale) == 100: continue
	process_timingpoint.append(classes.TimingPoint(timingpoint.offset, calcurate.inheritedpoint(equal_scale), beat, sample_set, sample_index, volume, True, effects))
	pass

process_parsed = classes.ParsedBeatmap(process_timingpoint, parsed_file.HitObjects)
# どうやらコンソールのパスからの指定らしい...
parser.parsesave(process_parsed, "./inheritedpoint.txt")
