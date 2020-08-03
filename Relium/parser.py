"""
.osuファイルパーサー
by @Komasan5364
"""
from typing import List, Optional
from .classes import ParsedBeatmap, TimingPoint, HitObject
from .convert import text_to_timingpoint, text_to_hitobject
from .export import timingpoint, hitobject

def parsefile(beatmap_path: str) -> ParsedBeatmap:
	"""
	osuファイルを解析してParsedBeatmapクラスを返します

	引数
	----
	beatmap_path : str
		-> osuファイルのパス

	戻り値
	------
	ParsedBeatmap
		-> ParsedBeatmapクラス

	予想される例外
	--------------
	FileNotFoundError
		-> パスにファイルが見つかりません、絶対パスの場合は``r"絶対パス"``を使うと良いかもしれません
	"""
	otp: List[TimingPoint] = []
	oho: List[HitObject] = []
	with open(beatmap_path, mode='r') as b:
		while not b.readline().startswith("[TimingPoints]"):
			pass
		while True:
			l = b.readline()
			if l.startswith("[HitObjects]"):
				break
			try:
				tp: TimingPoint = text_to_timingpoint(l)
				otp.append(tp)
			except ValueError:
				pass
		
		while True:
			lp = b.tell()
			l = b.readline().replace('\n', '').replace('\r', '')
			if lp == b.tell():
				break
			try:
				ho: HitObject = text_to_hitobject(l)
				oho.append(ho)
			except ValueError:
				pass
		
		return ParsedBeatmap(otp, oho)


def parsesave(parsed_beatmap: ParsedBeatmap, save_path: str) -> None:
	"""
	ParsedBeatmapクラスを指定したパスに保存します

	引数
	----
	parsed_beatmap : ParsedBeatmap
		-> ParsedBeatmapクラス
	save_path : str
		-> 保存するパス

	予想される例外
	--------------
	PermissionError
		-> 書き込むための権限がありません、諦めてください

	注意
	----
	これはosu fileとしてそのまま引用することはできません。 あくまでTimingPointとHitObjectだけを使用する前提で作られています
	"""
	with open(save_path, mode='w', encoding='utf-8') as b:
		b.write("[TimingPoints]\n")
		for tp in parsed_beatmap.TimingPoints:
			b.write(timingpoint(tp) + "\n")
		b.write("\n")
		b.write("[HitObjects]\n")
		for ho in parsed_beatmap.HitObjects:
			b.write(hitobject(ho) + "\n")
		b.write("\n")
