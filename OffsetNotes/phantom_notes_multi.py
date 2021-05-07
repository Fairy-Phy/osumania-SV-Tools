import Relium

osu_file = r""

parse_file = Relium.parsefile(osu_file)

changed_hitobjects = list()
for hitobject in parse_file.HitObjects:
	changed_hitobjects.append(Relium.HitObject(hitobject.key_position, 185014, True, hitobject.hitsound, hitobject.offset, hitobject.customsound))

Relium.parsesave(Relium.ParsedBeatmap(parse_file.TimingPoints, changed_hitobjects), "./export.txt")
