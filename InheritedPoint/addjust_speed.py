from Relium import calcurate, export, classes, parser

source_file = ""

parsed_file = parser.parsefile(source_file)

before_bpm = 170
after_bpm = 127.5

export_timingpoint = list()
for timingpoint in parsed_file.TimingPoints:
	if not timingpoint.inherited: continue
	export_timingpoint.append(classes.TimingPoint(timingpoint.offset, calcurate.inheritedpoint(calcurate.inheritedpoint(timingpoint.beat_length) * (after_bpm / before_bpm)), timingpoint.beat, timingpoint.sample_set, timingpoint.sample_index, timingpoint.volume, timingpoint.inherited, timingpoint.effects))

parser.parsesave(parser.ParsedBeatmap(export_timingpoint, list()), "./inheritedpoint.txt")
