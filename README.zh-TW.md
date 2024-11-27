# KK Unused Mods Remover/Packer

## 簡介
KK Unused Mods Remover/Packer 用於管理戀愛活動（簡稱戀活）中的未使用模組。該工具支援檢測未使用的模組，並進行移除、打包或還原操作。  
本工具支援以下語言（README.md文檔以及程式文字顯示皆為機器翻譯）：  
- [英文 (English)](README.en.md)  
- [繁體中文 (Traditional Chinese)](README.zh-TW.md)  
- [簡體中文 (Simplified Chinese)](README.zh-CN.md)  
- [日文 (Japanese)](README.ja.md)  
- [韓文 (Korean)](README.ko.md)  
- [俄文 (Russian)](README.ru.md)  

## 下載
- 從 [release](https://github.com/KKUnusedModsRemoverPacker/releases) 下載最新版本程式。  
- 解壓縮檔案，並執行 `KK_Unused_Mods_Remover.exe`。

## 使用步驟
1. **上傳mod數據csv**：
   - 開啟 KKManager -> 工具 -> Export to csv... -> Zipmod usage (including unused)  
     ![image](https://github.com/user-attachments/assets/38dfa3fd-14dd-459d-aef7-94d38aea2841)  
   - 上傳至 KK Unused Mods Remover/Packer 的 csv 檔案上傳區域。

2. **檢測未使用模組**：
   - 按下 `偵測` 按鈕，檢測是否有未使用到的模組。

3. **輸入模組路徑**：
   - 輸入模組所在資料夾，可手動輸入或使用 `瀏覽` 按鈕選擇。

4. **選取操作（Action）選單**：
   - 下拉式選單，包含以下選項：
     - **打包**：將未使用模組搬移到 `unused mods` 資料夾（若無則自動建立）。
     - **復原打包**：將搬移到 `unused mods` 的模組還原至原位置。
     - **移除**：移除所有檢測到的未使用模組（不會檢查 `unused mods` 資料夾）。

5. **僅限自訂模組核取方塊勾選**：
   - 勾選 `僅限自訂模組`，僅針對 `模組路徑` 根目錄中的模組進行操作，不會對子資料夾中的模組進行操作。

6. **執行所選的操作 (Action)**：
   - 按下 `執行` 按鈕，執行選定的操作。
  
## 注意事項
  - **刪除無法復原**，只有打包可以復原

## 可能遇到的問題
1. **被視為惡意程式**：
   - 請暫時關閉防毒軟體

## 不必要知道的細節
  - 原本就沒有卡片在使用的模組 ，打勾後依然'Cards with usages' 為0
  - 禁用模組不會改變'Cards with usages'數 
  - KKManager 輸出模組檔案中，同樣的'GUID'只輸出一個(應該是用字典排序決定輸出為何者，我用相同模組1,0和1.1版本測試，1.1版本也用了兩個不同檔案，結果只輸出1.0版本的此模組，此外，輸出順序與是否啟用模組無關)
  - 輸出不同版本的相同模組會對應到相同的'Cards with usages'數

## 開源協議
本程式依據 [GPL License](https://www.gnu.org/licenses/gpl-3.0.html) 開源。

## 聯絡我們
如有問題，歡迎透過 GitHub Issue 功能提交。
