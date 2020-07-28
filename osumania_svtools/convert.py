"""
いろいろな変換するやつ
"""

from .classes import TimingPoint, HitObject
from .constant import max_offset

def time_to_offset(time_text: str) -> int:
	"""
	テキストの時間からオフセット値に変換します

	引数
	----
	time_text: str
		-> 時間の文字列
	
	戻り値
	------
	int
		-> オフセット値

	使用例
	------
	```
	print(time_to_offset("02:31:465")) # 151465
	```

	予想される例外
	--------------
	ValueError
		-> おそらくフォーマットが合っていないです、時間の文字列というのはEditの左下から得られる時間のことです
	"""
	offset = int(0)
	list_count = int(0)
	for time_str in time_text.split(':'):
		if not time_str.isdigit():
			raise ValueError("Time text is not allowed format")

		time = int(time_str)
		if list_count == 0:
			offset += time * 60 * 1000
		elif list_count == 1:
			offset += time * 100
		elif list_count == 2:
			offset += time
		else:
			raise ValueError("Time text is not allowed format")

		list_count += 1
		pass

	return offset

def text_to_timingpoint(text: str) -> TimingPoint:
	"""
	TimingPointの文字列を各情報に変換してTimingPointクラスで出力します

	引数
	----
	text: str
		-> TimingPoint

	戻り値
	------
	TimingPoint
		-> TimingPointクラス

	予想される例外
	--------------
	ValueError
		-> おそらくフォーマットが合っていないです、一旦見直しましょう
	"""
	text_split: list = text.split(',')
	if len(text_split) != 8:
		raise ValueError("text is not allowed format")

	try:
		offset = int(text_split[0])
		beat = int(text_split[2])
		sample_set = int(text_split[3])
		sample_index = int(text_split[4])
		volume = int(text_split[5])
		inherited: bool = True if text_split[6] == 0 else False
		effects = int(text_split[7])

		beat_length = -float(text_split[1]) if inherited else float(text_split[1])

		return TimingPoint(offset, beat_length, beat, sample_set, sample_index, volume, inherited, effects)
	except ValueError:
		raise ValueError("text is not allowed format")

def text_to_hitobject(text: str) -> HitObject:
	"""
	HitObjectの文字列を各情報に変換してHitObjectクラスで出力します

	引数
	----
	text: str
		-> HitObject

	戻り値
	------
	HitObject
		-> HitObjectクラス

	予想される例外
	--------------
	ValueError
		-> おそらくフォーマットが合っていないです、一旦見直しましょう
	"""
	text_split: list = text.split(',')
	if len(text_split) != 6:
		raise ValueError("text is not allowed format")

	try:
		key_position = int(text_split[0])
		offset = int(text_split[2])
		LN: bool = True if text_split[3] == "128" else False
		hitsound = int(text_split[4])

		if LN:
			customsound_split: list = text_split[5].split(':')
			if len(customsound_split) != 6:
				raise ValueError("text is not allowed format")

			end_offset = int(customsound_split.pop(0))
			customsound: str = ':'.join(customsound_split)

			return HitObject(key_position=key_position, offset=offset, LN=LN, hitsound=hitsound, end_offset=end_offset, customsound=customsound)
		else:
			customsound: str = text_split[5]

			return HitObject(key_position=key_position, offset=offset, LN=LN, hitsound=hitsound, customsound=customsound)
	except ValueError:
		raise ValueError("text is not allowed format")


def voidobject(key_position: int, offset: int) -> HitObject:
	"""
	引数から判定のないヒットオブジェクト(シングルノーツのみ)のHitObjectクラスを生成します

	引数
	----
	key_position : int
		-> キーポジション、1から入れる場合はkey_assetから参照したものを入れてください

	offset : int
		-> (配置する)オフセット値

	戻り値
	------
	HitObject
		-> 空ノーツのHitObjectクラス
	"""
	return HitObject(key_position, max_offset, True, end_offset=offset)
