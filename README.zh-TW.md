# 戀活未使用模組移除/打包工具(KK Unused Mods Remover/Packer)

## 簡介
戀活未使用模組移除/打包工具(KK Unused Mods Remover/Packer)用於管理戀活(Koikatsu，簡寫為KK)中的未使用模組。該工具支援偵測未使用的模組，並進行移除、打包或還原操作。 
本工具支援以下語言（程式中顯示的文字為機器翻譯之結果）：  
- [English](README.md)  
- [繁體中文(Traditional Chinese)](README.zh-TW.md)  
- 简体中文(Simplified Chinese)  
- 日本語(Japanese)  
- 한국어(Korean)  
- Русский(Russian)  

## 下載
- 從 [release](https://github.com/paul0728/KKUnusedModsRemoverPacker/releases/) 下載最新版本程式。  
- 執行 `KK_mod_remover_packer_mutilang.exe`。

## 使用步驟
1. **上傳 mod 數據 csv**：
   - 開啟 [KKManager](https://github.com/IllusionMods/KKManager) -> `工具` -> `Export to csv...` -> `Zipmod usage(including unused)`
     
     ![image](https://github.com/user-attachments/assets/38dfa3fd-14dd-459d-aef7-94d38aea2841)  
   - 上傳至 KK Unused Mods Remover/Packer 的 csv 檔案上傳區域。

2. **檢測未使用模組**：
   - 按下 `偵測` 按鈕，偵測是否有未使用到的模組。

3. **輸入模組路徑**：
   - 輸入模組所在資料夾，可手動輸入或使用 `瀏覽` 按鈕選擇。

4. **選取操作（Action）選單**：
   - 下拉式選單，包含以下選項：
     - **打包**：將未使用模組搬移到 `unused mods` 資料夾（若無則自動建立）。
     - **復原打包**：將搬移到 `unused mods` 的模組還原至原位置。
     - **移除**：移除所有偵測到的未使用模組（不會對 `unused mods` 資料夾進行操作）。

5. **僅限自訂模組(Custom Mods Only)核取方塊勾選（可選擇）**：
   - **未勾選**：對整個模組資料夾（包含子資料夾）內之所有檔案進行操作。
   - **勾選**：`僅限自訂模組`，僅針對 `模組路徑` 根目錄中的模組進行操作，不會對子資料夾中的模組進行操作。

6. **執行所選的操作(Action)**：
   - 按下 `執行` 按鈕，執行選定的操作。
  
## 注意事項
  - 按下`移除`後會有確認訊息框跳出，然而 **`移除`無法復原**，只有打包可以復原，請謹慎使用。
  - 程式 **不會記錄** 上一次`打包`之模組原路徑，故`打包`後關閉程式，**下次開啟程式時無法復原`打包`**。

## 可能遇到的問題
1. **被視為惡意程式**：
   - 請暫時關閉防毒軟體。

## 不必要知道的細節
  - 原本就沒有卡片在使用的模組，打勾後依然 'Cards with usages' 為 0。
  - 禁用模組不會改變 'Cards with usages' 數。
  - KKManager 輸出模組檔案中，同樣的 'GUID' 只輸出一個（應該是用字典排序決定輸出為何者，我用相同模組 1.0 和 1.1 版本測試，1.1 版本也用了兩個不同檔案，結果只輸出 1.0 版本的此模組，此外，輸出順序與是否啟用該模組無關）。
  - 輸出不同版本的相同模組會對應到相同的 'Cards with usages' 數。

## 歡迎提交 PR
本專案為開源專案，歡迎貢獻您的改進建議或新增功能！如有任何改善程式碼的點子，請透過 Fork 本專案並提交 Pull Request(PR)。  

## 開源協議
本程式依據 [MIT License](https://opensource.org/licenses/MIT) 開源。

## 聯絡
如有問題，歡迎透過 GitHub Issue 功能提交。
