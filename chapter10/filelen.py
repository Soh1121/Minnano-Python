import sys                              # sysモジュールをインポート

for fn in sys.argv[1:]:                 # スクリプトの引数を取り出す
    try:
        f = open(fn)
    except FileNotFoundError:           # Python3.2は「IOError」に
        print("{}というファイルは存在しません".format(fn))
    else:
        try:
            print(fn, len(f.read()))    # ファイル名とサイズを表示
        finally:
            f.close()                   # ファイルをcloseする
