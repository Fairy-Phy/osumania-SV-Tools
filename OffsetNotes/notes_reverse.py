import Relium

osu_file = r""

parse_file = Relium.parsefile(osu_file)
parse_file.HitObjects.sort(key=lambda value: value.offset, reverse=False)

#* THIS IS 4K ONLY!!!!!!!!!!!!!!!!!!! *#

changed_hitobjects = list()
current_notes_temp = list()
prev_offset = 0
LN_end_matching_notes = 0
for hitobject_range in range(len(parse_file.HitObjects)):
	hitobject = parse_file.HitObjects[hitobject_range]

	if len(current_notes_temp) == 0:
		current_notes_temp.append(hitobject)
		prev_offset = hitobject.offset
		continue
	elif prev_offset == hitobject.offset:
		current_notes_temp.append(hitobject)
		continue
	elif prev_offset != hitobject.offset:
		#print(current_notes_temp)
		print(len(current_notes_temp))

		#- Main Processor -#

		def main_processor():
			keylist: list = Relium.constant.key_asset[4].copy()

			if len(current_notes_temp) == 1:
				keylist.remove(current_notes_temp[0].key_position)

				for key_position in keylist:
					changed_hitobjects.append(Relium.HitObject(key_position, current_notes_temp[0].offset, current_notes_temp[0].LN, current_notes_temp[0].hitsound, current_notes_temp[0].end_offset, current_notes_temp[0].customsound))
			elif len(current_notes_temp) == 2:
				notes_keylist_index = list()
				for temp_hitobject in current_notes_temp:
					notes_keylist_index.append(keylist.index(temp_hitobject.key_position))

				if (notes_keylist_index[0] == 0 and notes_keylist_index[1] == 3) or (notes_keylist_index[0] == 1 and notes_keylist_index[1] == 2) or (notes_keylist_index[0] == 0 and notes_keylist_index[1] == 2) or (notes_keylist_index[0] == 1 and notes_keylist_index[1] == 3):
					for temp_hitobject in current_notes_temp:
						keylist_index = keylist.index(temp_hitobject.key_position)
						if keylist_index == 0: keylist_index = 1
						elif keylist_index == 1: keylist_index = 0
						elif keylist_index == 2: keylist_index = 3
						elif keylist_index == 3: keylist_index = 2
						changed_hitobjects.append(Relium.HitObject(keylist[keylist_index], temp_hitobject.offset, temp_hitobject.LN, temp_hitobject.hitsound, temp_hitobject.end_offset, temp_hitobject.customsound))
				elif (notes_keylist_index[0] == 0 and notes_keylist_index[1] == 1) or (notes_keylist_index[0] == 2 and notes_keylist_index[1] == 3):
					for temp_hitobject in current_notes_temp:
						keylist_index = keylist.index(temp_hitobject.key_position)
						if keylist_index == 0: keylist_index = 3
						elif keylist_index == 1: keylist_index = 2
						elif keylist_index == 2: keylist_index = 1
						elif keylist_index == 3: keylist_index = 0
						changed_hitobjects.append(Relium.HitObject(keylist[keylist_index], temp_hitobject.offset, temp_hitobject.LN, temp_hitobject.hitsound, temp_hitobject.end_offset, temp_hitobject.customsound))
			elif len(current_notes_temp) == 3:
				LN_count = 0
				apply_notes = current_notes_temp[0]

				for temp_hitobject in current_notes_temp:
					keylist.remove(temp_hitobject.key_position)
					if temp_hitobject.LN:
						LN_count += 1
						if LN_count == 2:
							apply_notes = temp_hitobject

				for key_position in keylist:
					changed_hitobjects.append(Relium.HitObject(key_position, apply_notes.offset, apply_notes.LN, apply_notes.hitsound, apply_notes.end_offset, apply_notes.customsound))
			elif len(current_notes_temp) == 4:
				pass

		main_processor()

		#- Reset Temp -#
		current_notes_temp = list()
		current_notes_temp.append(hitobject)
		prev_offset = hitobject.offset
		if hitobject_range == len(parse_file.HitObjects) - 1:
			#print(current_notes_temp)
			print(len(current_notes_temp))
			main_processor()

Relium.parsesave(Relium.ParsedBeatmap(parse_file.TimingPoints, changed_hitobjects), "./export.txt")
