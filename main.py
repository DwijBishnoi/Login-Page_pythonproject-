import tkinter as tk
from tkinter import messagebox
import pymysql


class MainScr:
    def _init_(self):
        root = tk.Tk()
        self.root = root
        self.root.title("Student Assistant")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        label = tk.Label(root, text="Welcome To your Very own Student Assistant\nChoose From the Following:")
        label.config(font=("Times New Roman", 20), fg="white")
        label.pack()

        frame = tk.Frame(root, bg="dark gray")
        frame.pack(fill="both", expand=True)

        b1 = tk.Button(frame, text="Time Table", command=self.show_timetable)
        b2 = tk.Button(frame, text="Event Planner", command=self.show_event_planner)
        b3 = tk.Button(frame, text="Notes", command=self.show_notes)
        b4 = tk.Button(frame, text="Money Tracker", command=self.show_money_tracker)

        buttons = [b1, b2, b3, b4]
        for button in buttons:
            button.config(font=("Times New Roman", 12), width=20, height=2, bg="light gray")
            button.pack(pady=10)

    def show_timetable(self):
        # Implement the TimeTable functionality here
        TimeTable()

    def show_event_planner(self):
        # Implement the EventPlanner functionality here
        EventPlanner()

    def show_notes(self):
        # Implement the Notes functionality here
        Notes()

    def show_money_tracker(self):
        # Implement the Money Tracker functionality here
        MoneyTracker()


class TimeTable:
    def _init_(self):
        self.root = tk.Tk()
        self.root.title("Time Table")
        self.root.geometry("700x500")
        self.root.configure(bg="dark gray")

        try:
            con = pymysql.connect(host="localhost", user="root", password="1234", database="student_assistant")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM Time_Table;")
            data = cursor.fetchall()

            for row in data:
                for item in row[2:]:
                    text_box = tk.Entry(self.root, width=15)
                    text_box.insert(0, item)
                    text_box.configure(state="readonly")
                    text_box.pack(side="left")

            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {str(e)}")


class EventPlanner:
    def _init_(self):
        self.root = tk.Tk()
        self.root.title("Event Planner")
        self.root.geometry("400x400")
        self.root.configure(bg="dark gray")

        self.date = tk.StringVar()
        self.name = tk.StringVar()

        label = tk.Label(self.root, text="Event Date(YYYY-MM-DD):")
        label.pack()

        date_entry = tk.Entry(self.root, textvariable=self.date)
        date_entry.pack()

        label = tk.Label(self.root, text="Event Name:")
        label.pack()

        name_entry = tk.Entry(self.root, textvariable=self.name)
        name_entry.pack()

        submit_button = tk.Button(self.root, text="Submit", command=self.enter_database)
        submit_button.pack()

        display_button = tk.Button(self.root, text="Display Events", command=self.show_database)
        display_button.pack()

    def enter_database(self):
        # Implement the functionality to insert event data into the database here
        date = self.date.get()
        name = self.name.get()
        try:
            con = pymysql.connect(host="localhost", user="root", password="1234", database="student_assistant")
            cursor = con.cursor()
            cursor.execute("INSERT INTO Event_Planner (E_Date, E_Name) VALUES (%s, %s)", (date, name))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Event data has been inserted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {str(e)}")

    def show_database(self):
        # Implement the functionality to display events from the database here
        try:
            con = pymysql.connect(host="localhost", user="root", password="1234", database="student_assistant")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM Event_Planner;")
            data = cursor.fetchall()

            event_list = [f"{date}: {name}" for date, name in data]
            event_info = "\n".join(event_list)

            messagebox.showinfo("Events", event_info)
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {str(e)}")


class Notes:
    def _init_(self):
        self.root = tk.Tk()
        self.root.title("Notes")
        self.root.geometry("500x500")
        self.root.configure(bg="dark gray")

        self.note_title = tk.StringVar()
        self.note = tk.StringVar()

        title_label = tk.Label(self.root, text="Note Title:")
        title_label.pack()

        title_entry = tk.Entry(self.root, textvariable=self.note_title)
        title_entry.pack()

        note_label = tk.Label(self.root, text="Enter Note:")
        note_label.pack()

        note_entry = tk.Entry(self.root, textvariable=self.note)
        note_entry.pack()

        submit_button = tk.Button(self.root, text="Submit", command=self.enter_database)
        submit_button.pack()

        display_button = tk.Button(self.root, text="Display Notes", command=self.show_database)
        display_button.pack()

        self.button_frame = tk.Frame(self.root, bg="gray")
        self.button_frame.pack(fill="y", side="right")

        try:
            con = pymysql.connect(host="localhost", user="root", password="1234", database="student_assistant")
            cursor = con.cursor()
            cursor.execute("SELECT N_Title FROM Notes;")
            data = cursor.fetchall()

            for title in data:
                button = tk.Button(self.button_frame, text=title[0],
                                   command=lambda title=title[0]: self.display_note(title))
                button.pack()

            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {str(e)}")

    def enter_database(self):
        # Implement the functionality to insert notes into the database here
        note_title = self.note_title.get()
        note = self.note.get()
        try:
            con = pymysql.connect(host="localhost", user="root", password="1234", database="student_assistant")
            cursor = con.cursor()
            cursor.execute("INSERT INTO Notes (N_Title, Note) VALUES (%s, %s)", (note_title, note))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Note has been inserted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {str(e)}")

    def show_database(self):
        # Implement the functionality to display notes from the database here
        try:
            con = pymysql.connect(host="localhost", user="root", password="1234", database="student_assistant")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM Notes;")
            data = cursor.fetchall()

            notes_info = "\n".join([f"{title}: {note}" for title, note in data])
            messagebox.showinfo("Notes", notes_info)
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {str(e)}")

    def display_note(self, title):
        # Implement the functionality to display a specific note here
        try:
            con = pymysql.connect(host="localhost", user="root", password="1234", database="student_assistant")
            cursor = con.cursor()
            cursor.execute("SELECT Note FROM Notes WHERE N_Title = %s", (title,))
            data = cursor.fetchone()

            if data:
                messagebox.showinfo(title, data[0])
            else:
                messagebox.showerror("Error", "Note not found.")
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {str(e)}")


class MoneyTracker:
    def _init_(self):
        self.root = tk.Tk()
        self.root.title("Money Tracker")
        self.root.geometry("700x500")
        self.root.configure(bg="dark gray")

        try:
            con = pymysql.connect(host="localhost", user="root", password="1234", database="student_assistant")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM Money_Tracker;")
            data = cursor.fetchall()

            for row in data:
                for item in row[2:]:
                    text_box = tk.Entry(self.root, width=15)
                    text_box.insert(0, item)
                    text_box.configure(state="readonly")
                    text_box.pack(side="left")

            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {str(e)}")

MainScr().mainloop()