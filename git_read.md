1. 版本號
git version

2. 設定全域使用者
git config --global user.name name - 設定名稱
git config --global user.email email - 設定 eamil
git config --list - 查看設定

3. 初始化倉庫
git init

4. 倉庫狀態
U->Utracked

git status

5. 加入控管(暫存區)
git commit -m "註解"

6. 其餘狀態
U->Utracked
U->A (Added)
A->M (Modified)
A->D (Delete)

7. 刪除後恢復
git restore filename

8. 檢視暫存區
git ls-files -s

9. 檢視
git cat-file -t(型態) shall(前六碼)
             -p(內容)

10. 加入倉庫

11. 檢視 log