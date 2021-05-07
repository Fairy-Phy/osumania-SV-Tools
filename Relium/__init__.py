"""
Relium
======
これはosu!maniaのSVを作成するために作ったツールです、説明はすべて日本語で書かれています

説明は各モジュール・関数を参照してください

表記上の注意
------------
TimingPoint
	-> ``40719,250,4,0,0,100,1,0``のようなosuファイルの[TimingPoints]に書かれている文字列群のことを指します

タイミングポイント
	-> 赤線を形成するTimingPointの速度値のことです

インヘリテッドポイント
	-> 緑線を形成するTimingPointの速度値のことです、このツールではマイナス表記はしませんが文字列に直す際にマイナスは付きます

TimingPointクラス
	-> TimingPointを分解して1つ1つの情報として分けたクラスです

HitObject
	-> ``320,192,73257,1,10,0:0:0:0:``のようなosuファイルの[HitObjects]に書かれている文字列群のことを指します

HitObjectクラス
	-> HitObjectを分解して1つ1つの情報として分けたクラスです

空ノーツ
	-> 判定のないシングルノーツのことです。LNの始点を曲が終了するオフセット値よりも後に設置し、終点を設置したいオフセット値に置くことで作ることができます。ただしこれをすると理論スコアが変わってしまうため注意が必要です
"""

from .constant import zero_bpm, inf_bpm, max_offset, min_offset, key_asset
from .calcurate import timingpoint as calc_timingpoint
from .calcurate import inheritedpoint as calc_inheritedpoint
from .calcurate import line_notesposition as calc_line_notesposition
from .convert import time_to_offset
from .convert import text_to_timingpoint
from .convert import text_to_hitobject
from .export import timingpoint as export_timingpoint
from .export import hitobject as export_hitobject
from .export import voidobject as export_voidobject
from .classes import TimingPoint
from .classes import HitObject
from .classes import ParsedBeatmap
from .parser import parsefile
from .parser import parsesave
