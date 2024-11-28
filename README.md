⚠ **Name Change Notice**: To better reflect its functionality, this tool has been renamed from `KKUnusedModsRemoverPacker` to `KKModsCleaner`.

# KK Mods Cleaner

## Introduction
KK Mods Cleaner is a tool for managing mods in Koikatsu (KK). It supports detecting mods with usage below a user-defined threshold (minimum card usage count) and allows removal, packing, or restoration operations.  
This tool supports the following languages (text in the program is machine-translated):  
- [English](README.md)  
- [繁體中文 (Traditional Chinese)](README.zh-TW.md)  
- 简体中文 (Simplified Chinese)  
- 日本語 (Japanese)  
- 한국어 (Korean)  
- Русский (Russian)  

## Download
- Download the latest release from [releases](https://github.com/paul0728/KKUnusedModsRemoverPacker/releases/).  
- Run `KK_mods_cleaner.exe`.

## Steps to Use
1. **Upload Mod Data .csv file**:
   - Open [KKManager](https://github.com/IllusionMods/KKManager) -> Select a folder (e.g., male, female) -> `Tools` -> `Export to csv...` -> `Zipmod usage (including unused)`
     
     ![image](https://github.com/user-attachments/assets/38dfa3fd-14dd-459d-aef7-94d38aea2841)  
   - Upload the .csv file to KK Mods Cleaner in the file upload section.

2. **Set Threshold (Minimum Card Usage Count)**:
   - Default value: 0  
   - No restrictions on input range.

3. **Detect Unused Mods**:
   - Click the `Detect` button to find unused mods.
   - 'Detects' mods with card usage counts **below** or **equal to** the threshold.
   - After detection, the **minimum** and **maximum** card usage counts of the mods are displayed next to the threshold input box.

4. **Input Mod Path**:
   - Input the folder where the mods are located, either manually or using the `Browse` button.

5. **Select an Action**:
   - Use the dropdown menu to select one of the following actions:
     - **Pack**: Move unused mods to the `unused mods` folder (created automatically if it doesn’t exist).
     - **Restore Pack**: Restore mods moved to the `unused mods` folder back to their original location.
     - **Remove**: Delete all detected unused mods (does not affect the `unused mods` folder).

6. **Enable Custom Mods Only Checkbox (Optional)**:
   - **Unchecked**: Operates on all files in the mod folder (including subfolders).  
   - **Checked**: Limits actions to mods in the root of the `mod path` directory, excluding subfolders.

7. **Execute Selected Action**:
   - Click the `Execute` button to perform the selected action.

## Notes
- A confirmation dialog appears when clicking `Remove`. However, **`Remove` cannot be undone**. Only the Pack option is reversible, so use with caution.
- The program **does not record** the original paths of mods after packing. Therefore, if the program is closed after packing, **restoring packed mods will not be possible** the next time it is opened.

## Possible Issues
1. **Detected as Malware**:
   - Temporarily disable antivirus software.

## Details You Don't Need to Know
- Mods that are already unused will still show 'Cards with usages' as 0 even if the checkbox is checked.
- Disabling mods does not affect the 'Cards with usages' count.
- In KKManager’s exported mod file, only one 'GUID' per mod is exported (likely determined by dictionary order). Testing with versions 1.0 and 1.1 of the same mod shows that only version 1.0 is exported, regardless of whether version 1.1 includes additional files. Export order is also unrelated to mod activation status.
- Different versions of the same mod will correspond to the same 'Cards with usages' count.

## Contributing
This project is open-source. Contributions are welcome! If you have ideas for improvements or new features, please fork the project and submit a Pull Request (PR).

## License
This program is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contact
For questions, please use the GitHub Issues feature.
