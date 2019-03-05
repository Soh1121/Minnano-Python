# coding: utf-8

def guess_encoding(s):
    """
    バイト型の文字列を引数として受け取り、
    エンコードを簡易に判定する
    """
    # 判定を行うエンコードをリストに保存
    encodings = ["ascii", "utf-8", "shift-jis", "euc-jp"]
    for enc in encodings:
        try:
            s.decode(enc)   # エンコード変換を試みる
        except UnicodeDecodeError:
            continue        # エンコードに失敗したので次を試す
        else:
            return enc
            # エラーが発生しなかったら変換に成功したエンコードを返す
    else:
        return ""           # 成功したエンコードがなければから文字列を返す