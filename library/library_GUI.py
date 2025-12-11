import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class Library_GUI:
    def __init__(self, library_system):
        self.system = library_system
        self.root = None
        self.status_label = None
        self.tree_search = None
        self.text_report = None

    def run(self):
        self.root = tk.Tk()
        self.root.title("Library Management System")
        self.root.geometry("900x600")
        self.root.configure(bg="#f4f4f4")
        self.build_ui()
        self.status_label = tk.Label(self.root, text="", bg="#f4f4f4", fg="green", anchor="w")
        self.status_label.pack(fill="x", pady=5)
        self.root.mainloop()

    def build_ui(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill="both")

        # --- Add Book tab ---
        tab_add_book = ttk.Frame(notebook); notebook.add(tab_add_book, text="Add Book")
        tk.Label(tab_add_book, text="Add a New Book", font=("Arial", 16)).pack(pady=10)
        frame_book = tk.Frame(tab_add_book); frame_book.pack(pady=10)
        tk.Label(frame_book, text="Title:").grid(row=0, column=0, sticky="w")
        self.entry_b_title = tk.Entry(frame_book, width=40); self.entry_b_title.grid(row=0, column=1)
        tk.Label(frame_book, text="Author:").grid(row=1, column=0, sticky="w")
        self.entry_b_author = tk.Entry(frame_book, width=40); self.entry_b_author.grid(row=1, column=1)
        tk.Label(frame_book, text="ISBN:").grid(row=2, column=0, sticky="w")
        self.entry_b_isbn = tk.Entry(frame_book, width=40); self.entry_b_isbn.grid(row=2, column=1)
        tk.Button(tab_add_book, text="Add Book", command=self.add_book_gui, bg="#3399ff", fg="white").pack(pady=10)

        # --- Add Member tab ---
        tab_add_member = ttk.Frame(notebook); notebook.add(tab_add_member, text="Add Member")
        tk.Label(tab_add_member, text="Add a New Member", font=("Arial", 16)).pack(pady=10)
        frame_member = tk.Frame(tab_add_member); frame_member.pack(pady=10)
        tk.Label(frame_member, text="Name:").grid(row=0, column=0)
        self.entry_m_name = tk.Entry(frame_member, width=40); self.entry_m_name.grid(row=0, column=1)
        tk.Label(frame_member, text="Email:").grid(row=1, column=0)
        self.entry_m_email = tk.Entry(frame_member, width=40); self.entry_m_email.grid(row=1, column=1)
        tk.Button(tab_add_member, text="Add Member", command=self.add_member_gui, bg="#3399ff", fg="white").pack(pady=10)

        # --- Borrow tab ---
        tab_borrow = ttk.Frame(notebook); notebook.add(tab_borrow, text="Borrow Book")
        tk.Label(tab_borrow, text="Borrow Book", font=("Arial", 16)).pack(pady=10)
        frame_borrow = tk.Frame(tab_borrow); frame_borrow.pack(pady=10)
        tk.Label(frame_borrow, text="Member ID:").grid(row=0, column=0)
        self.entry_br_member = tk.Entry(frame_borrow, width=30); self.entry_br_member.grid(row=0, column=1)
        tk.Label(frame_borrow, text="Book ID:").grid(row=1, column=0)
        self.entry_br_book = tk.Entry(frame_borrow, width=30); self.entry_br_book.grid(row=1, column=1)
        tk.Button(tab_borrow, text="Borrow", command=self.borrow_book_gui, bg="#3399ff", fg="white").pack(pady=20)

        # --- Return tab ---
        tab_return = ttk.Frame(notebook); notebook.add(tab_return, text="Return Book")
        tk.Label(tab_return, text="Return Book", font=("Arial", 16)).pack(pady=10)
        frame_return = tk.Frame(tab_return); frame_return.pack(pady=10)
        tk.Label(frame_return, text="Member ID:").grid(row=0, column=0)
        self.entry_rt_member = tk.Entry(frame_return, width=30); self.entry_rt_member.grid(row=0, column=1)
        tk.Label(frame_return, text="Book ID:").grid(row=1, column=0)
        self.entry_rt_book = tk.Entry(frame_return, width=30); self.entry_rt_book.grid(row=1, column=1)
        tk.Button(tab_return, text="Return", command=self.return_book_gui, bg="#3399ff", fg="white").pack(pady=20)

        # --- Search tab ---
        tab_search = ttk.Frame(notebook); notebook.add(tab_search, text="Search Books")
        tk.Label(tab_search, text="Search Books", font=("Arial", 16)).pack(pady=10)
        self.entry_search = tk.Entry(tab_search, width=50); self.entry_search.pack()
        self.tree_search = ttk.Treeview(tab_search, columns=("ID","Title","Author"), show="headings")
        self.tree_search.pack(expand=True, fill="both", pady=10)
        for col in ("ID","Title","Author"): self.tree_search.heading(col, text=col)
        tk.Button(tab_search, text="Search", command=self.search_gui, bg="#3399ff", fg="white").pack()

        # --- Data save/load tab ---
        tab_data = ttk.Frame(notebook); notebook.add(tab_data, text="Save/Load Data")
        tk.Label(tab_data, text="Data Management", font=("Arial", 16)).pack(pady=10)
        tk.Button(tab_data, text="Save Data (JSON)", command=self.save_data_gui, bg="#3399ff", fg="white").pack(pady=5)
        tk.Button(tab_data, text="Load Data (JSON)", command=self.load_data_gui, bg="#3399ff", fg="white").pack(pady=5)
        tk.Button(tab_data, text="Reload UI (refresh)", command=self.refresh_ui, bg="#a2a2a2").pack(pady=5)

        # --- Export/Report tab ---
        tab_export = ttk.Frame(notebook); notebook.add(tab_export, text="Reports & Export")
        tk.Label(tab_export, text="Export Reports", font=("Arial", 16)).pack(pady=10)
        tk.Button(tab_export, text="Export CSV", command=self.export_csv, bg="#3399ff", fg="white").pack(pady=5)
        tk.Button(tab_export, text="Export PDF", command=self.export_pdf, bg="#3399ff", fg="white").pack(pady=5)
        tk.Button(tab_export, text="Generate Report", command=self.show_report, bg="#3399ff", fg="white").pack(pady=10)
        self.text_report = tk.Text(tab_export, height=20); self.text_report.pack(expand=True, fill="both")

        # initial UI state
        self.refresh_ui()

    # -------------------------
    # Helper / UI utilities
    # -------------------------
    def show_status(self, msg, color="green"):
        if self.status_label:
            self.status_label.config(text=msg, fg=color)
        else:
            print(msg)

    def refresh_ui(self):
        # Optionally could refresh lists / treeviews; here we clear search results
        if self.tree_search:
            self.tree_search.delete(*self.tree_search.get_children())

    # -------------------------
    # Actions wired to backend
    # -------------------------
    def add_book_gui(self):
        title = self.entry_b_title.get().strip()
        author = self.entry_b_author.get().strip()
        isbn = self.entry_b_isbn.get().strip()
        if not title or not author or not isbn:
            self.show_status("All fields required.", "red"); return
        bid = self.system.add_book(title, author, isbn)
        self.show_status(f"Book added (ID: {bid})")

    def add_member_gui(self):
        name = self.entry_m_name.get().strip()
        email = self.entry_m_email.get().strip()
        if not name or not email:
            self.show_status("All fields required.", "red"); return
        mid = self.system.add_member(name, email)
        self.show_status(f"Member added (ID: {mid})")

    def borrow_book_gui(self):
        mid = self.entry_br_member.get().strip(); bid = self.entry_br_book.get().strip()
        if not mid or not bid:
            self.show_status("Member ID and Book ID required.", "red"); return
        ok = self.system.borrow_book(mid, bid)
        if ok: self.show_status("Book borrowed successfully.")
        else: self.show_status("Borrow failed. Check IDs or availability.", "red")

    def return_book_gui(self):
        mid = self.entry_rt_member.get().strip(); bid = self.entry_rt_book.get().strip()
        if not mid or not bid:
            self.show_status("Member ID and Book ID required.", "red"); return
        ok = self.system.return_book(mid, bid)
        if ok: self.show_status("Book returned successfully.")
        else: self.show_status("Return failed. Check IDs.", "red")

    def search_gui(self):
        keyword = self.entry_search.get().strip()
        self.tree_search.delete(*self.tree_search.get_children())
        if not keyword:
            self.show_status("Enter a search keyword.", "red"); return
        results = self.system.search_books(keyword)
        if not results:
            self.show_status("No results found.", "red"); return
        for b in results:
            self.tree_search.insert("", "end", values=(b.book_id, b.title, b.author))
        self.show_status(f"{len(results)} result(s)")

    # -------------------------
    # Save / Load JSON (GUI)
    # -------------------------
    def save_data_gui(self):
        filename = filedialog.asksaveasfilename(
            title="Save JSON File", defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not filename: return
        ok = False
        try:
            ok = self.system.save_to_json(filename)
        except Exception as e:
            messagebox.showerror("Save error", f"Failed to save data:\n{e}")
            return
        if ok:
            self.show_status("Data saved successfully.")
        else:
            self.show_status("Data save failed.", "red")

    def load_data_gui(self):
        filename = filedialog.askopenfilename(title="Select JSON File", filetypes=[("JSON files", "*.json")])
        if not filename: return
        ok = False
        try:
            ok = self.system.load_from_json(filename)
        except Exception as e:
            messagebox.showerror("Load error", f"Failed to load data:\n{e}")
            return
        if ok:
            self.show_status("Data loaded successfully.")
            self.refresh_ui()
        else:
            self.show_status("Data load failed.", "red")

    # -------------------------
    # Export / Report
    # -------------------------
    def export_csv(self):
        try:
            ok = self.system.export_reports_to_csv()
        except Exception as e:
            messagebox.showerror("Export CSV error", f"{e}"); return
        if ok: self.show_status("CSV exported.")
        else: self.show_status("CSV export failed.", "red")

    def export_pdf(self):
        try:
            ok = self.system.export_reports_to_pdf()
        except Exception as e:
            messagebox.showerror("Export PDF error", f"{e}"); return
        if ok: self.show_status("PDF exported.")
        else: self.show_status("PDF export failed.", "red")

    def show_report(self):
        try:
            report = self.system.generate_report()
            self.text_report.delete("1.0", tk.END)
            self.text_report.insert(tk.END, report)
            self.show_status("Report generated.")
        except Exception as e:
            messagebox.showerror("Report error", f"{e}")
            self.show_status("Report generation failed.", "red")
