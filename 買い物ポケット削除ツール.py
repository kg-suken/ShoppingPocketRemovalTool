import winreg

def delete_registry_key(key_path):
    try:
        # キーを開く
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)
        
        # サブキーをすべて列挙して削除
        try:
            while True:
                subkey_name = winreg.EnumKey(key, 0)
                subkey_path = f"{key_path}\\{subkey_name}"
                delete_registry_key(subkey_path)
        except WindowsError:
            pass
        
        # キーを閉じる
        winreg.CloseKey(key)
        
        # 最終的にキーを削除
        winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, key_path)
        print(f"Registry key '{key_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"Registry key '{key_path}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")
        print("管理者権限で実行する必要があります")

# 削除したいレジストリキーのパスを指定します
key_path = r"SOFTWARE\WOW6432Node\Google\Chrome\Extensions\pgmbeccjfkdbpdjfoldaahpfamjjafma"

# レジストリキーを削除します
delete_registry_key(key_path)
