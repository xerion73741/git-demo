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
git add filename


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
git commit -m(messenger) "註解"


11. 檢視倉庫狀態
git log
git log --oneline


12. 暫存區檔案恢復工作目錄(U)
git restore --staged filename


13. 移除暫存區保留工作目錄(U)
git rm --cached filename


14. 強制刪除
git rm -f(force) filename


15. 產生分支
git branch name


16. 檢視分支
git branch


17. 切換分支
git checkout branch-nama


18. 捨棄變動
git checkout .


19. 合併分支
git merge test
到 master 去合併 test


20. 合併問題
選擇/修改檔案並 -am


21. 刪除分支
git branch -D test