def check_time():
    start_str = input('開始時間を入力: ')
    end_str = input('終了時間を入力: ')
    time_str = input('範囲内かどうか確認したい時間を入力: ')

    try:
    # stringに変換
        start_int = int(start_str)
        end_int = int(end_str)
        time_int = int(time_str)
    except ValueError:
        print('エラー: 半角数字で入力してください')

    # 不適な数値が入力された場合
    if not ((0 <= start_int < 24) and (0 <= end_int < 24) and (0 <= time_int < 24)):
        print('時間は0から23の数値で入力してください')
        return

    if start_int < end_int:
        if start_int <= time_int and time_int < end_int:
            # startとendのあいだにある場合
            print('時間範囲内に含まれています')
            return
    elif end_int < start_int:
        if start_int <= time_int or time_int < end_int:
            # 範囲が23時をまたぐ場合
            print('時間範囲内に含まれています')
            return
    else:
        if start_int == time_int:
            # startとendが同じ時間の場合
            print('時間範囲内に含まれています')
            return

    print('時間範囲内に含まれていません')
    return

check_time()