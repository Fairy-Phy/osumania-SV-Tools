"""
計算系
"""

from typing import Union
from . import constant

"""
説明: タイミングポイントとBPMを相互変換出来ます。タイミングポイントならBPMが、BPMならタイミングポイントが返ってきます
注意: 0を入れるとZeroDivisionErrorになるためconstant.zero_bpmやconstant.inf_bpmを使用してください

timingpoint_or_bpm: タイミングポイントかBPM
"""
def timingpoint(timingpoint_or_bpm: Union[float, int]) -> float:
	"""
	タイミングポイントとBPMを相互変換出来ます。タイミングポイントならBPMが、BPMならタイミングポイントが返ってきます

	注意
	----
	0を入れるとZeroDivisionErrorになるため``constant.zero_bpm``や``constant.inf_bpm``を使用してください

	引数
	----------
	timingpoint_or_bpm : float
		-> タイミングポイントかBPM

	戻り値
	-------
	float
		-> BPMかタイミングポイント

	予想される例外
	--------------
	ZeroDivisionError
		-> 0BPMなら``constant.zero_bpm``を、タイミングポイントが``0``なら``constant.inf_bpm``を使用してください
	"""
	return 60000.00 / timingpoint_or_bpm

def inheritedpoint(inheritedpoint_or_scale: Union[float, int]) -> float:
	"""
	インヘリテッドポイントと倍率を相互変換出来ます。インヘリテッドポイントなら倍率が、倍率ならインヘリテッドポイントが返ってきます

	注意
	----
	0を入れるとZeroDivisionErrorになるため``constant.zero_bpm``や``constant.inf_bpm``を使用してください

	引数
	----------
	inheritedpoint_or_scale : float
		-> インヘリテッドポイントか倍率

	戻り値
	-------
	float
		-> 倍率かインヘリテッドポイント

	予想される例外
	--------------
	ZeroDivisionError
		-> 倍率が``0x``なら``constant.zero_bpm``を、インヘリテッドポイントが``0``なら``constant.inf_bpm``を使用してください
	"""
	return 100.00 / inheritedpoint_or_scale

def line_notesposition(avgbpm: Union[float, int], ms: Union[float, int]) -> float:
	"""
	1offsetで移動する距離のタイミングポイントを返します

	注意
	----
	1, msは速度設定やスキンによって大きく変わります。 例えばデフォルトスキンの速度設定20(固定), BPMが60の場合、msが570が最大で見える範囲内になります

	2, これは『1offsetで移動する距離』になります、2offset以上の場合``1オフセットのms / offset``を計算してからmsを入力してください。 注意1のms = 570を引用すると5offset開けて同じ位置に置くのであれば``570 / 5``をするとそれがmsになります。 しかし、offsetの間隔を開ければ開けるほどキレがなくなるので非推奨です

	引数
	----------
	avgbpm : Union[float, int]
		-> 平均BPMです。 0-∞(155)と表記されている場合括弧に入っている数値を入力します
	
	ms : Union[float, int]
		-> 判定位置からどこまで移動するか

	戻り値
	-------
	float
		-> 1offsetで移動する距離のタイミングポイント

	予想される例外
	--------------
	ZeroDivisionError
		-> avgbpmやmsが0の場合に発生します。 0BPMでは移動できません、0msなら``constant.zero_bpm``を参照してください
	"""
	return 60000.00 / (avgbpm * ms)
