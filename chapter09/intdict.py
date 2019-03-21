class IntDict(dict):
    """ ディクショナリ型を継承してクラスを作る
    """
    def __init__(self):
        pass

    def __setitem__(self, key, value):
        """ 特殊メソッドをオーバーライド
            keyがint型以外なら例外を発生
        """
        if not isinstance(key, int):
                # キーが文字列でない場合には例外を発生
                raise ValueError("Key must be int.")
                # スーパークラスの特殊メソッドを呼び出し、キーと値を設定
        dict.__setitem__(self, key, value)
