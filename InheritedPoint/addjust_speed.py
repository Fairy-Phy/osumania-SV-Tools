from Relium import calcurate, export, classes, parser

"""
before_bpmからafter_bpmに変更されたときの緑線の倍率変更をします
"""

source_file = r""

parsed_file = parser.parsefile(source_file)

before_bpm = 200
after_bpm = 250

export_timingpoint = list()
for timingpoint in parsed_file.TimingPoints:
	if not timingpoint.inherited: continue
	export_timingpoint.append(classes.TimingPoint(timingpoint.offset, calcurate.inheritedpoint(calcurate.inheritedpoint(timingpoint.beat_length) * (after_bpm / before_bpm)), timingpoint.beat, timingpoint.sample_set, timingpoint.sample_index, timingpoint.volume, timingpoint.inherited, timingpoint.effects))

parser.parsesave(parser.ParsedBeatmap(export_timingpoint, list()), "./inheritedpoint.txt")
