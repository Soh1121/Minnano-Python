def guess_encoding(s):
    """
    バイト型の文字列を引数として受け取り，
    エンコードを簡易に判定する
    """
    #判定を行うエンコードをリストに保存
    encodings = ["ascii", "utf-8", "shift-jis", "euc-jp" ]
    for enc in encodings:
        try:
            s.decode(enc)  # エンコード変換を試みる
        except UnicodeDecodeError,e:
            continue       # エンコード変換に失敗したので次を試す
        else:
            return enc
                  # 変換に成功したエンコードを返す
    return ""          # 成功したエンコードがなければ空の文字列を返す
