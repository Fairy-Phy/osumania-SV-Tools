"""
.osuファイルパーサー
"""

from .classes import ParsedBeatmap, TimingPoint, HitObject

def parsefile(beatmap_path: str) -> ParsedBeatmap:
	"""
	作成中

	Parameters
	----------
	beatmap_path : str
		[description]

	Returns
	-------
	ParsedBeatmap
		[description]
	"""
	# pathからBeatmapを読み込みTimingPointとHitObjectを解析しParsedBeatmapで返す
	pass


def parsesave(parsed_beatmap: ParsedBeatmap, save_path: str) -> None:
	"""
	作成中

	Parameters
	----------
	parsed_beatmap : ParsedBeatmap
		[description]
	save_path : str
		[description]
	"""
	# ParsedBeatmapをもとに戻しsave_pathに入れるだけ
	pass
