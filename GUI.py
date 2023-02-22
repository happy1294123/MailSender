from MailSender import MailSender
import tkinter as tk
from tkinter import ttk, messagebox
# - Fund Id
# - Fund Name
# - Rule Name
# - Note 
# - Occurred

class GUI:
    def __init__(self):
        root = tk.Tk()
        root.geometry('600x600')
        root.title('mail sender')

        frame = tk.Frame(root)
        frame.columnconfigure(0, weight=2)
        frame.columnconfigure(1, weight=2)
        frame.columnconfigure(2, weight=2)
        frame.columnconfigure(3, weight=2)
        frame.columnconfigure(4, weight=2)
        frame.columnconfigure(5, weight=2)
        tk.Label(frame, text="Fund ID").grid(row=0, column=0, padx=10, pady=10)
        self.fund_id = tk.Entry(frame, width="30")
        self.fund_id.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(frame, text="Fund Name").grid(row=1, column=0, padx=10, pady=10)
        self.fund_name = tk.Entry(frame, width="30")
        self.fund_name.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(frame, text="Rule Name").grid(row=2, column=0, padx=10, pady=10)
        self.rule_name = tk.Entry(frame, width="30")
        self.rule_name.grid(row=2, column=1, padx=10, pady=10)
        tk.Label(frame, text="Note").grid(row=3, column=0, padx=10, pady=10)
        self.note = tk.Entry(frame, width="30")
        self.note.grid(row=3, column=1, padx=10, pady=10)
        tk.Label(frame, text="Occurred").grid(row=4, column=0, padx=10, pady=10)
        self.occurred = tk.Entry(frame, width="30")
        self.occurred.grid(row=4, column=1, padx=10, pady=10)
        frame.pack()

        # test val
        self.fund_id.insert(0, 'id')
        self.fund_name.insert(0, 'name')
        self.rule_name.insert(0, 'r_name')
        self.note.insert(0, 'note')
        self.occurred.insert(0, '2023-02-11 18:00:00')
        
        all_frame = tk.Frame(root)
        all_frame.columnconfigure(0, weight=1)
        all_frame.columnconfigure(1, weight=1)
        tk.Label(all_frame, text="All Date").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        tk.Text(all_frame, height=8, width=60).grid(row=1, column=0, pady=(0, 30))
        # all_frame.pack()

        choice_frame = tk.Frame(root)
        choice_frame.columnconfigure(0, weight=2)
        choice_frame.columnconfigure(0, weight=1)
        tk.Label(choice_frame, text="Fix day").grid(row=2, column=0, padx=10, pady=10)
        self.fix = ttk.Combobox(choice_frame, value=[
                "5 days",
                "6 days",
                "3 weeks",
                "1 month"
            ], width="28")
        self.fix.grid(row=2, column=1, padx=(24,0))
        self.checkbox = tk.IntVar()
        tk.Checkbutton(choice_frame, text="PM ratify", variable=self.checkbox).grid(row=3, column=1, padx=(0, 50), pady=10)
        choice_frame.pack()

        tk.Button(root, text="執行", command=self.handle_btn).pack()
        self.res = tk.StringVar()
        tk.Label(root, textvariable=self.res).pack()

        root.mainloop()

    def handle_btn(self):
        try:
            fix = {
                '5 days': '5d',
                '6 days': '6d',
                '3 weeks': '3w',
                '1 month': '1m'
            }[self.fix.get()]
            data = {
                'fid': self.fund_id.get(),
                'fname': self.fund_name.get(),
                'rname': self.rule_name.get(),
                'note': self.note.get(),
                'occurred': self.occurred.get(),
                'fix': fix,
                'pm_ratify': self.checkbox.get()
            }
        except:
            messagebox.showinfo(title="錯誤訊息", message='輸入資料有誤')
            return;

        mail_sender = MailSender(data);
        mail_sender.write_mail();
        

# GUI()







