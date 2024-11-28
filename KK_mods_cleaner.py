# KK Mods Cleaner
# Copyright (c) 2024 [Your Name or Organization]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import csv
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, Frame, Label, Entry, Button, Checkbutton, BooleanVar, StringVar
import tkinterdnd2 as tkdnd
import chardet
import sys
class Localizations:
    LANGUAGES = {
        'en': {
            'title': 'KK Mods Cleaner',
            'upload_text': 'Drag and drop your CSV file here or click to upload',
            'detect': 'Detect',
            'mod_path': 'Mod Path',
            'action': 'Action',
            'custom_mods': 'Custom Mods Only',
            'min_usages': 'Minimum Card Usages',
            'run': 'Run',
            'browse': 'Browse',
            'action_pack': 'Pack',
            'action_undo_pack': 'Undo Pack',
            'action_remove': 'Remove',
            'language': 'Language:',
            'error_csv_upload': 'Only .csv files are allowed.',
            'error_upload': 'Upload Error',
            'error_no_csv': 'Please upload a CSV file first.',
            'error_mod_path': 'Please enter mod path',
            'error_invalid_path': 'The entered path is invalid.',
            'error_no_min_usage': 'Please enter minimum card usages.',
            'error_no_detection': 'Please detect first.',
            'result_all_used': 'All mods have card usages above the minimum.',
            'result_low_usage_found': '{} mods found with card usages at or below the minimum.',
            'nothing_to_remove': 'Nothing to remove.',
            'nothing_to_pack': 'Nothing to pack.',
            'confirm_remove': 'Are you sure you want to remove {} mod(s) with usage count at or below {}?',
            'confirm_remove_title': 'Confirm Remove',
            'success_pack': 'Pack executed successfully! {} mods moved.',
            'success_remove': 'Remove executed successfully! {} mods removed.',
            'success_undo_pack': 'Undo Pack executed successfully! {} mods restored.',
            'error_pack': 'Failed to pack mods: {}',
            'error_remove': 'Failed to remove mods: {}',
            'error_undo_pack': 'Failed to undo pack: {}',
            'error_unknown_action': 'Unknown action selected.',
            'nothing_to_undo': 'Nothing to undo.',
            'error_no_data': 'No data found in CSV.',
            'success_csv_upload': 'CSV uploaded successfully!'
        },
        'zh-tw': {
            'title': 'KK 模組清理工具',
            'upload_text': '將 CSV 檔案拖曳至此處或點擊上傳',
            'detect': '偵測',
            'mod_path': '模組路徑',
            'action': '操作',
            'custom_mods': '僅限自訂模組',
            'min_usages': '最小卡片使用次數',
            'run': '執行',
            'browse': '瀏覽',
            'action_pack': '打包',
            'action_undo_pack': '復原打包',
            'action_remove': '移除',
            'language': '語言：',
            'error_csv_upload': '只能上傳 .csv 檔案',
            'error_upload': '上傳錯誤',
            'error_no_csv': '請先上傳 CSV 檔案',
            'error_mod_path': '請輸入模組路徑',
            'error_invalid_path': '輸入的路徑無效',
            'error_no_min_usage': '請輸入最小卡片使用次數',
            'error_no_detection': '請先進行偵測',
            'result_all_used': '所有模組使用次數皆高於最小值',
            'result_low_usage_found': '找到 {} 個使用次數低於或等於最小值的模組',
            'nothing_to_remove': '沒有可移除的項目',
            'nothing_to_pack': '沒有可打包的項目',
            'confirm_remove': '您確定要移除 {} 個使用次數在{}次以下的模組嗎？',
            'confirm_remove_title': '確認移除',
            'success_pack': '打包執行成功！已移動 {} 個模組。',
            'success_remove': '移除執行成功！已移除 {} 個模組。',
            'success_undo_pack': '復原打包執行成功！已還原 {} 個模組。',
            'error_pack': '打包模組失敗：{}',
            'error_remove': '移除模組失敗：{}',
            'error_undo_pack': '復原打包失敗：{}',
            'error_unknown_action': '選擇了未知的操作。',
            'nothing_to_undo': '沒有可復原的項目',
            'error_no_data': 'CSV 檔案中沒有發現任何資料。',
            'success_csv_upload': 'CSV 上傳成功！'
        },
        'zh-cn': {
            'title': 'KK 模组清理工具',
            'upload_text': '将 CSV 文件拖拽至此处或点击上传',
            'detect': '检测',
            'mod_path': '模组路径',
            'action': '操作',
            'custom_mods': '仅限自定义模组',
            'min_usages': '最小卡片使用次数',
            'run': '执行',
            'browse': '浏览',
            'action_pack': '打包',
            'action_undo_pack': '撤销打包',
            'action_remove': '移除',
            'language': '语言：',
            'error_csv_upload': '只能上传 .csv 文件',
            'error_upload': '上传错误',
            'error_no_csv': '请先上传 CSV 文件',
            'error_mod_path': '请输入模组路径',
            'error_invalid_path': '输入的路径无效',
            'error_no_min_usage': '请输入最小卡片使用次数',
            'error_no_detection': '请先进行检测',
            'result_all_used': '所有模组使用次数均高于最小值',
            'result_low_usage_found': '找到 {} 个使用次数低于或等于最小值的模组',
            'nothing_to_remove': '没有可移除的项目',
            'nothing_to_pack': '没有可打包的项目',
            'confirm_remove': '您确定要移除 {} 个使用次数在{}次以下的模组吗？',
            'confirm_remove_title': '确认移除',
            'success_pack': '打包执行成功！已移动 {} 个模组。',
            'success_remove': '移除执行成功！已移除 {} 个模组。',
            'success_undo_pack': '撤销打包执行成功！已还原 {} 个模组。',
            'error_pack': '打包模组失败：{}',
            'error_remove': '移除模组失败：{}',
            'error_undo_pack': '撤销打包失败：{}',
            'error_unknown_action': '选择了未知的操作。',
            'nothing_to_undo': '没有可撤销的项目',
            'error_no_data': 'CSV 文件中没有发现任何数据。',
            'success_csv_upload': 'CSV 上传成功！'
        },
        'ja': {
            'title': 'KK MODクリーナー',
            'upload_text': 'CSVファイルをここにドラッグ＆ドロップするかアップロード',
            'detect': '検出',
            'mod_path': 'MODパス',
            'action': 'アクション',
            'custom_mods': 'カスタムMODのみ',
            'min_usages': '最小カード使用回数',
            'run': '実行',
            'browse': '参照',
            'action_pack': 'パック',
            'action_undo_pack': 'パックを取り消す',
            'action_remove': '削除',
            'language': '言語：',
            'error_csv_upload': '.csvファイルのみ許可されています',
            'error_upload': 'アップロードエラー',
            'error_no_csv': 'まずCSVファイルをアップロードしてください',
            'error_mod_path': 'MODパスを入力してください',
            'error_invalid_path': '入力されたパスは無効です',
            'error_no_min_usage': '最小カード使用回数を入力してください',
            'error_no_detection': '先に検出を実行してください',
            'result_all_used': 'すべてのMODの使用回数が最小値を上回っています',
            'result_low_usage_found': '使用回数が最小値以下のMODが {} 個見つかりました',
            'nothing_to_remove': '削除するものがありません',
            'nothing_to_pack': 'パックするものがありません',
            'confirm_remove': '使用回数が{}回以下のMOD {} 個を削除してもよろしいですか？',
            'confirm_remove_title': '削除の確認',
            'success_pack': 'パックが正常に実行されました！ {} 個のMODが移動されました。',
            'success_remove': '削除が正常に実行されました！ {} 個のMODが削除されました。',
            'success_undo_pack': 'パックの取り消しが正常に実行されました！ {} 個のMODが復元されました。',
            'error_pack': 'MODのパックに失敗しました：{}',
            'error_remove': 'MODの削除に失敗しました：{}',
            'error_undo_pack': 'パックの取り消しに失敗しました：{}',
            'error_unknown_action': '未知のアクションが選択されました。',
            'nothing_to_undo': '取り消すものがありません',
            'error_no_data': 'CSVにデータが見つかりません。',
            'success_csv_upload': 'CSVのアップロードに成功しました！'
        },
        'ko': {
            'title': 'KK 모드 클리너',
            'upload_text': 'CSV 파일을 여기에 끌어다 놓거나 클릭하여 업로드',
            'detect': '감지',
            'mod_path': '모드 경로',
            'action': '작업',
            'custom_mods': '사용자 지정 모드만',
            'min_usages': '최소 카드 사용 횟수',
            'run': '실행',
            'browse': '찾아보기',
            'action_pack': '패킹',
            'action_undo_pack': '패킹 취소',
            'action_remove': '제거',
            'language': '언어:',
            'error_csv_upload': '.csv 파일만 허용됩니다',
            'error_upload': '업로드 오류',
            'error_no_csv': '먼저 CSV 파일을 업로드하세요',
            'error_mod_path': '모드 경로를 입력하세요',
            'error_invalid_path': '입력한 경로가 잘못되었습니다',
            'error_no_min_usage': '최소 카드 사용 횟수를 입력하세요',
            'error_no_detection': '먼저 감지를 실행하세요',
            'result_all_used': '모든 모드의 사용 횟수가 최소값보다 높습니다',
            'result_low_usage_found': '사용 횟수가 최소값 이하인 모드 {} 개 발견',
            'nothing_to_remove': '제거할 항목 없음',
            'nothing_to_pack': '패킹할 항목 없음',
            'confirm_remove': '사용 횟수가 {}회 이하인 모드 {} 개를 제거하시겠습니까?',
            'confirm_remove_title': '제거 확인',
            'success_pack': '패킹 실행 성공! {} 개 모드 이동됨.',
            'success_remove': '제거 실행 성공! {} 개 모드 제거됨.',
            'success_undo_pack': '패킹 취소 실행 성공! {} 개 모드 복원됨.',
            'error_pack': '모드 패킹 실패: {}',
            'error_remove': '모드 제거 실패: {}',
            'error_undo_pack': '패킹 취소 실패: {}',
            'error_unknown_action': '선택한 작업이 알 수 없음',
            'nothing_to_undo': '취소할 항목 없음',
            'error_no_data': 'CSV 파일에 데이터가 없습니다.',
            'success_csv_upload': 'CSV 업로드 성공!'
        },
        'ru': {
            'title': 'KK Очиститель модов',
            'upload_text': 'Перетащите CSV-файл сюда или нажмите для загрузки',
            'detect': 'Обнаружить',
            'mod_path': 'Путь к модам',
            'action': 'Действие',
            'custom_mods': 'Только пользовательские моды',
            'min_usages': 'Минимальное количество использований карт',
            'run': 'Выполнить',
            'browse': 'Обзор',
            'action_pack': 'Упаковка',
            'action_undo_pack': 'Отмена упаковки',
            'action_remove': 'Удаление',
            'language': 'Язык:',
            'error_csv_upload': 'Разрешены только файлы .csv',
            'error_upload': 'Ошибка загрузки',
            'error_no_csv': 'Сначала загрузите CSV-файл',
            'error_mod_path': 'Введите путь к модам',
            'error_invalid_path': 'Введён неверный путь',
            'error_no_min_usage': 'Введите минимальное количество использований карт',
            'error_no_detection': 'Сначала выполните обнаружение',
            'result_all_used': 'Все моды используются выше минимума',
            'result_low_usage_found': 'Найдено {} модов с использованием не выше минимума',
            'nothing_to_remove': 'Нечего удалять',
            'nothing_to_pack': 'Нечего упаковывать',
            'confirm_remove': 'Вы уверены, что хотите удалить {} модов с количеством использований не более {}?',
            'confirm_remove_title': 'Подтвердить удаление',
            'success_pack': 'Упаковка выполнена успешно! Перемещено {} модов.',
            'success_remove': 'Удаление выполнено успешно! Удалено {} модов.',
            'success_undo_pack': 'Отмена упаковки выполнена успешно! Восстановлено {} модов.',
            'error_pack': 'Не удалось упаковать моды: {}',
            'error_remove': 'Не удалось удалить моды: {}',
            'error_undo_pack': 'Не удалось отменить упаковку: {}',
            'error_unknown_action': 'Неизвестное действие',
            'nothing_to_undo': 'Нечего отменять',
            'error_no_data': 'В CSV не найдены данные.',
            'success_csv_upload': 'CSV успешно загружен!'
        }
    }



class KKModTool:
    def __init__(self, master):

        self.master = master
        
        # Language selection
        self.current_language = StringVar(value='en')
        self.current_language.trace('w', self.change_language)

        # Configure main window
        self.master.title(self.get_localized_text('title'))
        self.master.iconbitmap(self.get_resource_path("KK_mods_cleaner_icon.ico"))
        self.master.geometry("600x550")  # 調整視窗高度
        self.master.configure(bg='#f0f0f0')

        # Style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', background='#4CAF50', foreground='white')
        self.style.configure('TCombobox', background='white')

        # Initialize variables
        self.csv_file = None
        self.detection_performed = False  # 新增偵測標誌
        self.low_usage_mods = []
        self.mod_path = None
        self.moved_files = {}

        # Create UI
        self.create_widgets()

        # Configure as drop target
        master.drop_target_register(tkdnd.DND_FILES)
        master.dnd_bind('<<Drop>>', self.handle_drop)



    def get_resource_path(self, relative_path):
        """
        獲取資源的絕對路徑，兼容 PyInstaller 的打包方式。
        """
        try:
            # PyInstaller 將資源打包到一個臨時文件夾中
            base_path = sys._MEIPASS
        except AttributeError:
            # 在未打包的開發環境中，使用相對路徑
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)



    def handle_drop(self, event):
        """Handle file drop event"""
        dropped_file = event.data
        # Remove curly braces and quotes if present
        dropped_file = dropped_file.strip('{}').strip('"')
        
        # Check if file is CSV
        if dropped_file.lower().endswith('.csv'):
            self.load_csv(dropped_file)
        else:
            messagebox.showerror(
                self.get_localized_text('error_upload'), 
                self.get_localized_text('error_csv_upload')
            )

    def get_localized_text(self, key, *args):
        """Get localized text for the current language"""
        lang = self.current_language.get()
        text = Localizations.LANGUAGES.get(lang, Localizations.LANGUAGES['en']).get(key, key)
        return text.format(*args) if args else text

    def update_ui_elements(self):
        self.master.title(self.get_localized_text('title'))
        self.language_label.config(text=self.get_localized_text('language'))
        self.drop_area.config(text=self.get_localized_text('upload_text'))
        self.detect_button.config(text=self.get_localized_text('detect'))
        self.path_label.config(text=self.get_localized_text('mod_path'))
        self.browse_button.config(text=self.get_localized_text('browse'))
        self.action_label.config(text=self.get_localized_text('action'))
        self.custom_checkbox.config(text=self.get_localized_text('custom_mods'))
        self.min_usages_label.config(text=self.get_localized_text('min_usages'))  # 新增此行
        self.run_button.config(text=self.get_localized_text('run'))

        # 更新 action combo 的選項
        actions = [
            self.get_localized_text('action_pack'),
            self.get_localized_text('action_undo_pack'),
            self.get_localized_text('action_remove')
        ]
        self.action_combo.config(values=actions)
        
        # 保持原本選擇的索引
        self.action_combo.current(self.current_action_index)

        # 更新顯示的文字
        self.action_combo_var.set(actions[self.current_action_index])


    # 添加新方法來追蹤選擇的變化
    def on_action_change(self, *args):
        self.current_action_index = self.action_combo.current()
    def change_language(self, *args):
        # 在更新UI之前記住當前選擇
        if hasattr(self, 'action_combo'):
            self.current_action_index = self.action_combo.current()
        self.update_ui_elements()

    def safe_move_file(src, dest):
        base, ext = os.path.splitext(dest)
        counter = 1
        while os.path.exists(dest):
            dest = f"{base}_{counter}{ext}"
            counter += 1
        shutil.move(src, dest)
        return dest



    def create_widgets(self):
        """建立 UI 元件，修正語言顯示為母語並確保語言切換功能正常"""
        # Main frame
        main_frame = Frame(self.master, bg='#f0f0f0')
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)

        # Language Selector
        language_frame = Frame(main_frame, bg='#f0f0f0')
        language_frame.pack(fill='x', pady=(0, 10))

        self.language_label = Label(
            language_frame,
            text=self.get_localized_text('language'),
            bg='#f0f0f0'
        )
        self.language_label.pack(side='left', padx=(0, 10))


        # Minimum Card Usages Selection
        min_usages_frame = Frame(main_frame, bg='#f0f0f0')
        min_usages_frame.pack(pady=5)

        self.min_usages_label = Label(
            min_usages_frame,
            text=self.get_localized_text('min_usages'),
            bg='#f0f0f0'
        )
        self.min_usages_label.pack(side='left')

        self.min_usages_var = StringVar(value='0')
        self.min_usages_entry = Entry(
            min_usages_frame,
            textvariable=self.min_usages_var,
            width=5
        )
        self.min_usages_entry.pack(side='left', padx=(0, 10))

        self.usage_range_label = Label(
            min_usages_frame,
            text='',
            bg='#f0f0f0'
        )
        self.usage_range_label.pack(side='left')

        # 顯示語言名稱對應的母語
        language_display_names = {
            'en': 'English',
            'zh-tw': '繁體中文',
            'zh-cn': '简体中文',
            'ja': '日本語',
            'ko': '한국어',
            'ru': 'Русский'
        }

        # 建立語言切換邏輯
        self.language_combo = ttk.Combobox(
            language_frame,
            state='readonly',
            values=[language_display_names[lang] for lang in Localizations.LANGUAGES.keys()],
            width=10
        )
        # 根據 current_language 設定當前選中值
        current_language_index = list(Localizations.LANGUAGES.keys()).index(self.current_language.get())
        self.language_combo.current(current_language_index)
        self.language_combo.pack(side='left')

        # 綁定語言切換事件
        def on_language_change(event):
            selected_index = self.language_combo.current()
            selected_language = list(Localizations.LANGUAGES.keys())[selected_index]
            self.current_language.set(selected_language)  # 更新 current_language 值
            self.change_language()  # 手動觸發語言更新

        self.language_combo.bind("<<ComboboxSelected>>", on_language_change)

        # CSV Upload Area (Drag and Drop)
        self.drop_area = tk.Label(
            main_frame,
            text=self.get_localized_text('upload_text'),
            bg='white',
            fg='gray',
            font=('Arial', 12),
            width=50,
            height=10,
            relief='groove',
            borderwidth=2
        )
        self.drop_area.pack(pady=10, padx=10, fill='both', expand=True)
        self.drop_area.bind("<Button-1>", self.upload_csv)

        # Detect Button
        self.detect_button = Button(
            main_frame,
            text=self.get_localized_text('detect'),
            command=self.detect_low_usage_mods
        )
        self.detect_button.pack(pady=5)

        # Mod Path
        path_frame = Frame(main_frame, bg='#f0f0f0')
        path_frame.pack(pady=5, padx=10, fill='x')

        self.path_label = Label(
            path_frame,
            text=self.get_localized_text('mod_path'),
            bg='#f0f0f0'
        )
        self.path_label.pack(side='top', anchor='w')

        self.path_input = Entry(path_frame, width=40)
        self.path_input.pack(side='left', expand=True, fill='x', padx=(0, 10))
        self.path_input.bind('<KeyRelease>', self.manual_mod_path_input)

        self.browse_button = Button(
            path_frame,
            text=self.get_localized_text('browse'),
            command=self.browse_mod_path
        )
        self.browse_button.pack(side='right')

        # Action Selection
        action_frame = Frame(main_frame, bg='#f0f0f0')
        action_frame.pack(pady=5)

        self.action_label = Label(
            action_frame,
            text=self.get_localized_text('action'),
            bg='#f0f0f0'
        )
        self.action_label.pack(side='top')

        self.action_combo_var = StringVar()
        self.action_combo = ttk.Combobox(
            action_frame,
            textvariable=self.action_combo_var,
            state="readonly"
        )
        self.action_combo.pack(pady=5)
        
        # 設定下拉選單選項
        actions = [
            self.get_localized_text('action_pack'),
            self.get_localized_text('action_undo_pack'),
            self.get_localized_text('action_remove')
        ]
        self.action_combo.config(values=actions)
        
        # 固定設置為第一個選項 (pack/打包)
        self.action_combo.current(0)
        self.current_action_index = 0

        # Custom Mods Checkbox
        custom_mods_frame = Frame(main_frame, bg='#f0f0f0')
        custom_mods_frame.pack(pady=5)

        self.custom_mods_var = BooleanVar()
        self.custom_checkbox = Checkbutton(
            custom_mods_frame,
            text=self.get_localized_text('custom_mods'),
            variable=self.custom_mods_var,
            bg='#f0f0f0'
        )
        self.custom_checkbox.pack()

        # Run Button
        self.run_button = Button(
            main_frame,
            text=self.get_localized_text('run'),
            command=self.execute_action
        )
        self.run_button.pack(pady=5)






    def upload_csv(self, event=None):
        file_path = filedialog.askopenfilename(
            title="Upload CSV", 
            filetypes=[("CSV Files", "*.csv")]
        )
        if file_path and file_path.endswith('.csv'):
            self.load_csv(file_path)

    def detect_csv_encoding(self, file_path):
        """檢測 CSV 文件的編碼"""

        # 使用 chardet 檢測文件編碼
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
            return result['encoding'] or 'utf-8'


    def load_csv(self, file_path):
        try:
            # 偵測編碼
            encoding = self.detect_csv_encoding(file_path)

            # 使用檢測到的編碼讀取檔案
            with open(file_path, 'r', encoding=encoding) as f:
                csv_reader = csv.reader(f)
                next(csv_reader)  # 跳過第一列 (column names)
                next(csv_reader)  # 跳過第二列

                data = []
                for row in csv_reader:
                    if len(row) >= 4:
                        cleaned_row = {
                            'GUID': row[0].strip(),
                            'Cards with usages': row[1].strip(),
                            'Is installed': row[2].strip(),
                            'Zipmod filename': row[3].strip()
                        }
                        data.append(cleaned_row)

                if not data:
                    raise ValueError(self.get_localized_text("error_no_data"))

                self.csv_file = data
                self.drop_area.config(text=self.get_localized_text("success_csv_upload"))
        except Exception as e:
            messagebox.showerror(
                self.get_localized_text("error_upload"),
                f"{self.get_localized_text('error_upload')}: {str(e)}"
            )



    def browse_mod_path(self):
        directory = filedialog.askdirectory(title="Select Mod Path")
        if directory:
            self.path_input.delete(0, tk.END)
            self.path_input.insert(0, directory)
            self.mod_path = directory

    def manual_mod_path_input(self, event=None):
        path = self.path_input.get().strip()
        if os.path.exists(path) and os.path.isdir(path):
            self.mod_path = path


    def detect_low_usage_mods(self):
        # ... 偵測邏輯 ...
        self.detection_performed = True  # 設置標誌
        if self.csv_file is None:
            messagebox.showerror(
                self.get_localized_text("error_upload"), 
                self.get_localized_text("error_no_csv")
            )
            return
        

        # 檢查是否輸入最小使用次數
        if not self.min_usages_var.get().strip():
            messagebox.showerror(
                self.get_localized_text("error_upload"), 
                self.get_localized_text("error_no_min_usage")
            )
            return
        
        try:
            min_usages = int(self.min_usages_var.get())
        except ValueError:
            messagebox.showerror(
                self.get_localized_text("error_upload"), 
                self.get_localized_text("error_no_min_usage")
            )
            return
        
        min_usages = int(self.min_usages_var.get())


        
        # 獲取新的低使用次數清單
        new_low_usage = []
        usages = []
        for mod in self.csv_file:
            usage = int(mod['Cards with usages'])
            usages.append(usage)
            if mod['Is installed'] == 'Yes' and usage <= min_usages:
                new_low_usage.append(mod['Zipmod filename'])

        # 更新低使用次數mod清單
        self.low_usage_mods = new_low_usage

        if usages:
            min_usage = min(usages)
            max_usage = max(usages)
            self.usage_range_label.config(text=f"({min_usage}, {max_usage})")
        else:
            self.usage_range_label.config(text="")

        if not self.low_usage_mods:
            messagebox.showinfo(
                self.get_localized_text("result_title"), 
                self.get_localized_text("result_all_used")
            )
        else:
            messagebox.showinfo(
                self.get_localized_text("result_title"), 
                self.get_localized_text("result_low_usage_found", len(self.low_usage_mods))
            )

    def count_packable_mods(self):
        return self.count_mods_for_action('pack')

    def count_removable_mods(self):
        return self.count_mods_for_action('remove')

    def count_mods_for_action(self, action):
        count = 0
        low_usage_folder = os.path.normpath(os.path.join(self.mod_path, "low_usage_mods"))

        if self.custom_mods_var.get():
            files = os.listdir(self.mod_path)
            count = sum(1 for file in files if file in self.low_usage_mods and os.path.isfile(os.path.join(self.mod_path, file)))
        else:
            for root, dirs, files in os.walk(self.mod_path):
                if os.path.abspath(root) == os.path.abspath(low_usage_folder):
                    continue
                count += sum(1 for file in files if file in self.low_usage_mods)

        return count

    def execute_action(self):
        """執行用戶選擇的操作"""

        # 使用標誌來檢查是否已執行偵測
        if not self.detection_performed:
            messagebox.showerror(
                self.get_localized_text("error_upload"),
                self.get_localized_text("error_no_detection")
            )
            return
        
        # 檢查模組路徑的有效性

        # 從文字方塊中取得當前模組路徑
        mod_path_input = self.path_input.get().strip()

        # 如果輸入為空，顯示錯誤訊息
        if not mod_path_input:
            messagebox.showerror(
                self.get_localized_text("error_upload"),
                self.get_localized_text("error_mod_path")
            )
            return  # 阻止執行

        # 如果輸入不為空，檢查路徑是否有效
        if not os.path.exists(mod_path_input) or not os.path.isdir(mod_path_input):
            messagebox.showerror(
                self.get_localized_text("error_upload"),
                self.get_localized_text("error_invalid_path")  # 新增本地化訊息
            )
            return  # 阻止執行

        # 更新模組路徑變數為當前輸入
        self.mod_path = mod_path_input

        # 獲取當前選中的操作
        selected_action = self.action_combo_var.get()

        # 比對操作並執行對應功能
        if selected_action == self.get_localized_text('action_remove'):
            remove_count = self.count_removable_mods()
            if remove_count == 0:
                messagebox.showinfo(
                    self.get_localized_text("nothing_to_remove_title"),
                    self.get_localized_text("nothing_to_remove")
                )
                return
            if self.confirm_action("remove", remove_count, int(self.min_usages_var.get())):
                self.remove_low_usage_mods()
        elif selected_action == self.get_localized_text('action_pack'):
            pack_count = self.count_packable_mods()
            if pack_count == 0:
                messagebox.showinfo(
                    self.get_localized_text("nothing_to_pack_title"),
                    self.get_localized_text("nothing_to_pack")
                )
                return
            self.pack_low_usage_mods(pack_count)
        elif selected_action == self.get_localized_text('action_undo_pack'):
            self.undo_pack()
        else:
            messagebox.showerror(
                self.get_localized_text("error_upload"),
                self.get_localized_text("error_unknown_action")
            )

    def confirm_action(self, action_type, count, min_usages=None):
        """確認操作（多語言支持）"""
        if action_type == "remove":
            return messagebox.askyesno(
                self.get_localized_text(f"confirm_{action_type}_title"),
                self.get_localized_text(f"confirm_{action_type}", count, min_usages)
            )
        return messagebox.askyesno(
            self.get_localized_text(f"confirm_{action_type}_title"),
            self.get_localized_text(f"confirm_{action_type}", count)
        )
    def pack_low_usage_mods(self, count=None):
        try:
            if not self.low_usage_mods:
                messagebox.showinfo(
                    self.get_localized_text("success_title"),
                    self.get_localized_text("nothing_to_pack")
                )
                return

            if not self.mod_path:
                messagebox.showerror(
                    self.get_localized_text("error_pack_title"),
                    self.get_localized_text("error_pack", "Mod path not specified")
                )
                return

            low_usage_folder = os.path.normpath(os.path.join(self.mod_path, "low_usage_mods"))
            os.makedirs(low_usage_folder, exist_ok=True)

            # 獲取已經在low_usage_folder中的文件名稱
            existing_moved = set()
            if os.path.exists(low_usage_folder):
                existing_moved = set(os.listdir(low_usage_folder))

            # 修改moved_files的初始化方式
            if not hasattr(self, 'moved_files'):
                self.moved_files = {}

            moved_count = 0

            if self.custom_mods_var.get():
                files = [f for f in os.listdir(self.mod_path) 
                        if os.path.isfile(os.path.join(self.mod_path, f)) and 
                        f in self.low_usage_mods and
                        f not in existing_moved]
                
                for file in files:
                    mod_path = os.path.normpath(os.path.join(self.mod_path, file))
                    destination_path = os.path.normpath(os.path.join(low_usage_folder, file))
                    if os.path.exists(mod_path):
                        shutil.move(mod_path, destination_path)
                        # 只記錄最新的來源路徑
                        self.moved_files[destination_path] = mod_path
                        moved_count += 1
            else:
                for root, dirs, files in os.walk(self.mod_path):
                    if os.path.abspath(root).startswith(os.path.abspath(low_usage_folder)):
                        continue

                    for file in files:
                        if file in self.low_usage_mods and file not in existing_moved:
                            mod_path = os.path.normpath(os.path.join(root, file))
                            destination_path = os.path.normpath(os.path.join(low_usage_folder, file))
                            if os.path.exists(mod_path):
                                shutil.move(mod_path, destination_path)
                                # 只記錄最新的來源路徑
                                self.moved_files[destination_path] = mod_path
                                moved_count += 1

            messagebox.showinfo(
                self.get_localized_text("success_title"),
                self.get_localized_text("success_pack", moved_count)
            )
        except Exception as e:
            messagebox.showerror(
                self.get_localized_text("error_pack_title"),
                self.get_localized_text("error_pack", str(e))
            )



    def remove_low_usage_mods(self):
        """移除低使用次數的模組（多語言支持）"""
        try:
            if not self.low_usage_mods:
                messagebox.showerror(
                    self.get_localized_text("error_remove_title"),
                    self.get_localized_text("nothing_to_remove")
                )
                return

            removed_count = 0
            low_usage_folder = os.path.normpath(os.path.join(self.mod_path, "low_usage_mods"))

            if self.custom_mods_var.get():
                files = os.listdir(self.mod_path)
                for file in files:
                    mod_path = os.path.normpath(os.path.join(self.mod_path, file))
                    if os.path.isfile(mod_path) and file in self.low_usage_mods:
                        os.remove(mod_path)
                        removed_count += 1
            else:
                for root, dirs, files in os.walk(self.mod_path):
                    if os.path.abspath(root) == os.path.abspath(low_usage_folder):
                        continue

                    for file in files:
                        if file in self.low_usage_mods:
                            mod_path = os.path.normpath(os.path.join(root, file))
                            os.remove(mod_path)
                            removed_count += 1

            messagebox.showinfo(
                self.get_localized_text("success_title"),
                self.get_localized_text("success_remove", removed_count)
            )
        except Exception as e:
            messagebox.showerror(
                self.get_localized_text("error_remove_title"),
                self.get_localized_text("error_remove", str(e))
            )
    def undo_pack(self):
        try:
            # 檢查是否有記錄
            if not self.moved_files:
                messagebox.showerror(
                    self.get_localized_text("error_undo_pack_title"), 
                    self.get_localized_text("nothing_to_undo")
                )
                return

            # 檢查 low_usage_mods 資料夾是否存在
            low_usage_folder = os.path.normpath(os.path.join(self.mod_path, "low_usage_mods"))
            if not os.path.exists(low_usage_folder):
                messagebox.showerror(
                    self.get_localized_text("error_undo_pack_title"), 
                    self.get_localized_text("nothing_to_undo")
                )
                return

            # 檢查是否有任何檔案可以還原
            files_to_restore = []
            for dest_path, source_path in self.moved_files.items():
                # 只有當目標檔案存在且原始位置不存在時才需要還原
                if os.path.exists(dest_path) and not os.path.exists(source_path):
                    files_to_restore.append((dest_path, source_path))

            if not files_to_restore:
                messagebox.showerror(
                    self.get_localized_text("error_undo_pack_title"), 
                    self.get_localized_text("nothing_to_undo")
                )
                return

            # 執行還原
            restored_count = 0
            for dest_path, source_path in files_to_restore:
                try:
                    os.makedirs(os.path.dirname(source_path), exist_ok=True)
                    shutil.move(dest_path, source_path)
                    # 成功還原後，從 moved_files 中移除這筆記錄
                    if dest_path in self.moved_files:
                        del self.moved_files[dest_path]
                    restored_count += 1
                except Exception as e:
                    # 如果單個檔案還原失敗，繼續處理其他檔案
                    continue

            if restored_count > 0:
                messagebox.showinfo(
                    self.get_localized_text("success_title"), 
                    self.get_localized_text("success_undo_pack", restored_count)
                )

        except Exception as e:
            messagebox.showerror(
                self.get_localized_text("error_undo_pack_title"), 
                self.get_localized_text("error_undo_pack", str(e))
            )
def main():
    root = tkdnd.Tk()
    app = KKModTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()