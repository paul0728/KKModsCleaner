# KK Unused Mods Remover/Packer

## Introduction
The **KK Unused Mods Remover/Packer** is a tool designed for managing unused mods in Koikatsu (KK). This tool supports detecting unused mods and provides options to remove, pack, or restore them.  
The tool supports the following languages (the program's text is machine-translated):  
- [English](README.md)  
- [繁體中文(Traditional Chinese)](README.zh-TW.md)  
- 简体中文(Simplified Chinese)  
- 日本語(Japanese)  
- 한국어(Korean)  
- Русский(Russian)  

## Download
- Download the latest version from the [releases page](https://github.com/paul0728/KKUnusedModsRemoverPacker/releases/).  
- Execute `KK_mod_remover_packer_mutilang.exe`.

## How to Use
1. **Upload mod data CSV**:
   - Open [KKManager](https://github.com/IllusionMods/KKManager) -> Select folder(e.g., male, female) -> `Tools` -> `Export to csv...` -> `Zipmod usage (including unused)`  
     
     ![image](https://github.com/user-attachments/assets/38dfa3fd-14dd-459d-aef7-94d38aea2841)  
   - Upload the generated CSV file to the upload section of the KK Unused Mods Remover/Packer.

2. **Detect unused mods**:
   - Click the `Detect` button to identify any unused mods.

3. **Input mod path**:
   - Specify the folder where your mods are stored. You can manually enter the path or select it using the `Browse` button.

4. **Select an action (Action menu)**:
   - Use the dropdown menu to choose one of the following options:
     - **Pack**: Move all unused mods to an `unused mods` folder (it will be created if it doesn't already exist).
     - **Undo Pack**: Restore mods previously moved to the `unused mods` folder back to their original location.
     - **Remove**: Delete all detected unused mods (this will not affect the `unused mods` folder).

5. **Check "Custom Mods Only" (optional)**:
   - **Unchecked**: Perform actions on all mods within the folder (including subfolders).
   - **Checked**: Restrict actions to mods located directly in the root folder of the specified mod path. Subfolders will be ignored.

6. **Execute the selected action**:
   - Click the `Run` button to perform the chosen action.

## Notes
- Clicking `Remove` will display a confirmation dialog. However, **`Remove` actions cannot be undone**. Only `Pack` actions can be undone, so use caution.
- The program **does not record** the original paths of mods moved during the `Pack` action. If you close the program, **the `Undo Pack` option will no longer be available**.

## Potential Issues
1. **Flagged as malicious software**:
   - Temporarily disable your antivirus software if it flags the program.

## Unnecessary Details
- Mods that were not originally used by any cards will still show 'Cards with usages' as 0 even if the `Custom Mods Only` option is selected.
- Disabling a mod will not change its 'Cards with usages' count.
- KKManager exports only one instance of a mod with the same 'GUID' (likely determined by dictionary order). In tests with the same mod in versions 1.0 and 1.1 (with 1.1 containing different files), only version 1.0 was exported. Export order is unrelated to whether the mod is enabled.
- Different versions of the same mod will have the same 'Cards with usages' count.

## Contributing
This project is open-source, and we welcome contributions! If you have ideas for improvements or new features, please fork the repository and submit a Pull Request (PR).

## License
This program is released under the [MIT License](https://opensource.org/licenses/MIT).

## Contact
For any issues, please use the GitHub Issues section to report them.
