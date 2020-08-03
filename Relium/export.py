"""
osuファイルのフォーマットに出力する系
"""

from typing import Union
from .constant import max_offset, key_asset
from .classes import TimingPoint, HitObject

def timingpoint(timing_point: TimingPoint) -> str:
	"""
	TimingPointクラスからTimingPointを生成します

	引数
	----
	timing_point : TimingPoint
		-> TimingPointクラス

	戻り値
	------
	str
		-> TimingPoint
	"""
	if timing_point.inherited:
		return "{0},-{1},{2},{3},{4},{5},0,{6}".format(timing_point.offset, timing_point.beat_length, timing_point.beat, timing_point.sample_set, timing_point.sample_index, timing_point.volume, timing_point.effects)
	else:
		return "{0},{1},{2},{3},{4},{5},1,{6}".format(timing_point.offset, timing_point.beat_length, timing_point.beat, timing_point.sample_set, timing_point.sample_index, timing_point.volume, timing_point.effects)

def hitobject(hit_object: HitObject) -> str:
	"""
	HitObjectクラスからHitObjectを生成します

	引数
	----
	hit_object: HitObject
		-> HitObjectクラス

	戻り値
	------
	str
		-> HitObject
	"""
	if hit_object.LN:
		return "{0},192,{1},128,{2},{3}:{4}".format(hit_object.key_position, hit_object.offset, hit_object.hitsound, hit_object.end_offset, hit_object.customsound)
	else:
		return "{0},192,{1},1,{2},{3}".format(hit_object.key_position, hit_object.offset, hit_object.hitsound, hit_object.customsound)

def voidobject(key: int, position: int, offset: int) -> str:
	"""
	引数から判定のないヒットオブジェクト(シングルノーツのみ)の文字列を生成します

	引数
	----
	key : int
		-> キーの数 (4K の場合は 4と入力)

	position : int
		-> 設置する位置 (例: 4Kの場合 0|1|2|3 で指定する)

	offset : int
		-> (配置する)オフセット値

	戻り値
	------
	str
		-> HitObject
	"""
	return "{0},192,{1},128,0,{2}:0:0:0:0:".format(key_asset[key][position], max_offset, offset)
