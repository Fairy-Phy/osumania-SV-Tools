"""
クラス置き場
"""

from typing import NamedTuple, Optional, Union, List

class TimingPoint(NamedTuple):
	"""
	```
	TimingPoint(offset: int, beat_length: Union[float, int], beat: int = 4, sample_set: int = 0, sample_index: int = 0, volume: int = 100, inherited: bool = False, effects: int = 0)
	```

	NamedTuple継承のTimingPointクラス

	引数・属性
	----
	offset : int
		-> オフセット値

	beat_length : Union[float, int]
		-> タイミングポイント ※ 緑線の場合はインヘリテッドポイント(マイナスは付けないでください)

	beat : int, optional
		-> 拍子数, 初期値は 4

	sample_set : int, optional
		-> サンプルセット(0 = ビートマップの初期値, 1 = normal, 2 = soft, 3 = drum), 初期値は 0

	sample_index : int, optional
		-> カスタムヒットサウンドの設定値(0 = デフォルトヒットサウンド), 初期値は 0

	volume : int, optional
		-> 音量, 初期値は 100

	inherited : bool, optional
		-> 緑線→True, 赤線→False, 初期値は False

	effects : int, optional
		-> エフェクト値(0 = Kiai modeにしない, 1 = Kiai modeにする, 2 = 最初の拍子線をなくしKiai modeにしない, 3 = 最初の拍子線をなくしKiai modeにする), 初期値は 0

	"""
	offset: int
	beat_length: Union[float, int]
	beat: int = 4
	sample_set: int = 0
	sample_index: int = 0
	volume: int = 100
	inherited: bool = False
	effects: int = 0


class HitObject(NamedTuple):
	"""
	```
	HitObject(key_position: int, offset: int, LN: bool = False, hitsound: int = 0, end_offset: Optional[int] = None, customsound: str = "0:0:0:0:")
	```

	NamedTuple継承のHitObjectクラス

	引数・属性
	----------
	key_position : int
		-> キーポジション、1から入れる場合はkey_assetから参照したものを入れてください

	offset : int
		-> (開始)オフセット値

	LN : bool, optional
		-> シングルノーツ→False, LN→True, 初期値は False

	hitsound : int, optional
		-> 必要なヒットサウンドの値を足した合計値 (0 = Normal, 2 = Whistle, 3 = Finish, 4 = Clap), 初期値は 0

	end_offset : Optional[int], optional
		-> 終了オフセット値 ※LNがTrueの場合のみ指定してください, 初期値は 0

	customsound : str, optional
		-> ``通常のサンプルセット : 追加サンプルセット : サンプルインデックス : 音量 : 音声ファイル名``, 初期値は "0:0:0:0:"

	customsoundの補足
	-----------------
	通常のサンプルセット と 追加サンプルセット は
	
	0 = サンプルセットなし

		通常の場合タイミングポイントのサンプルセットを継承します


		追加の場合は通常のサンプルセットを継承します

	1 = Normal

	2 = Soft

	3 = Drum
	"""
	key_position: int
	offset: int
	LN: bool = False
	hitsound: int = 0
	end_offset: Optional[int] = None
	customsound: str = "0:0:0:0:"

class ParsedBeatmap(NamedTuple):
	"""
	作成中
	"""
	TimingPoints: List[TimingPoint]
	HitObjects: List[HitObject]