"""
***************************************************************
* Name: Digital Forensic Informational Reference (DFIR) 
* Author: Andrew May
* Created: 10/30/2023
* Course: CIS 152 - Data Structures
* Version: 1.0.0
* OS: macOS Ventura 13.4
* IDE: VSCode - Version: 1.83.1 (Universal)
* Copyright: This is my own original work
* based on specifications issued by our instructor
* Description: DFIR is an easy-to-use, GUI-enabled tool 
* that allows students to quickly and reliably complete 
* any numeral system conversion (binary, decimal, hexadecimal), 
* byte swap operation (Big Endian, Little Endian), or file signature 
* lookup that their NET373 assignments may require.
* Input: Decimal, binary, and hexadecimal values
* Output: Converted numeric values and file signatures
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""

import tkinter
from ast import literal_eval
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import datetime

# If you need to change GUI widget colors for any reason, please do so right here!
# All visible components are controlled by (at least) one of these four color variables.
button_color = "black"
bg_color = "#3F3F42"
font_color = "white"
text_box = "black"


def current_date():
    """
        This function determines and returns the current date/time (UTC).
    """
    current_time = str(datetime.datetime.utcnow())
    time_string = "Session Start Date/Time (UTC): " + current_time
    return time_string


class Stack:
    def __init__(self):
        """
            Creates a new, empty stack.
        """
        self.stack = []

    def push(self, item):
        """
            Adds another item to the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
            Removes and returns an item from the stack.
        """
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        """
            If stack is empty, this method returns true.
        """
        return len(self.stack) == 0

    def size(self):
        """
            Returns length (size) of stack.
        """
        return len(self.stack)

    def top(self):
        """
            Returns top value in stack.
        """
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def print_stack_up(self):
        """
            Returns a string representation of the stack.
        """
        stack_string = ""
        if self.is_empty():
            return None
        for i in self.stack:
            if i != "":
                stack_string += i + '\n'
        return stack_string


class HashTable:
    def __init__(self, size=1):
        """
            Create empty list of given size.
        """
        self.size = size
        self.hash_table = self.create_container()

    def create_container(self):
        """
            Creates an empty HashTable container/bucket.
        """
        return [[]]

    def set_value(self, key, value):
        """
            Inserts values into HashTable.
        """
        hashed_key = hash(key) % self.size
        container = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(container):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
           container[index] = (key, value)
        else:
           container.append((key, value))

    def get_value(self, key):
        """
            Return searched value with specific key.
        """
        hashed_key = hash(key) % self.size
        container = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(container):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
            if found_key:
                return record_value
            else:
                return "No record found"
        
    def insertion_sort(self):
        """
            Sorting the hash map using insertion sort.
        """
        for container in self.hash_table:
            for i in range(1, len(container)):
                key, value = container[i]
                j = i - 1
                while j >= 0 and container[j][0] > key:
                    container[j + 1] = container[j]
                    j -= 1
                container[j + 1] = (key, value)

    def print_hash_table(self):
        """
            Prints the items contained within the HashTable.
        """
        return "\n".join(f"{str(container[i][0])}: {str(container[i][1])}" for container in self.hash_table for i in range(len(container)))


class HexTranslator:
    """
        This class contains all the code needed for 
        hexadecimal <-> decimal translation.
    """
    hex_set = set("1234567890ABCDEFabcdef ")
    dec_set = set("1234567890")

    @staticmethod
    def clear_entry1():
        """
            Deletes/clears the contents of entry1.
        """
        entry1.delete(0, 'end')

    @staticmethod
    def clear_hex():
        """
            Deletes/clears the contents of hex output textbox.
        """
        hex_out.delete('1.0', 'end')

    @staticmethod
    def remove_spaces(string):
        """
            Removes spaces from user-generated hexadecimal input.
        """
        return string.replace(" ", "")

    @staticmethod
    def swap_endian():
        """
            Converts 'Big Endian' values to 'Little Endian' values, 
            and vice versa.
        """
        HexTranslator.clear_hex()
        string = entry1.get()
        if string == "":
            HexTranslator.output_hex("ERROR: Input cannot be empty!")
        else:
            string = HexTranslator.remove_spaces(string)
            if HexTranslator.hex_set.issuperset(string) and len(string) % 2 == 0:
                ba = bytearray.fromhex(string)
                ba.reverse()
                HexTranslator.clear_entry1()
                endian = ba.hex()
                endian = endian.upper()
                HexTranslator.output_endian(endian)
            else:
                HexTranslator.output_hex("ERROR: Invalid hex value!")

    @staticmethod
    def output_endian(string):
        """
            Replaces original hex value in entry1
        """
        entry1.insert(END, string)

    @staticmethod
    def output_hex(string):
        """
            Prints generated output to the appropriate text box
        """
        hex_out.insert(END, string)

    @staticmethod
    def hex_to_dec():
        """
            Performs unsigned hex to dec conversion 
            (includes input validation).
        """
        global entry1, hex_out
        hex_string = entry1.get()
        HexTranslator.clear_hex()
        if hex_string == "":
            HexTranslator.output_hex("Dec:  NaN")
        else:
            if str(hex_string).startswith("0x"):
                HexTranslator.output_hex("Please remove '0x' from hex string!")
            else:
                hex_string = HexTranslator.remove_spaces(hex_string)
                if HexTranslator.hex_set.issuperset(hex_string):
                    hex_string = "0x" + str(hex_string)
                    hex_string.upper()
                    dec_num = literal_eval(hex_string)
                    HexTranslator.output_hex(f"Dec:  {dec_num}")
                    ConversionHistory.push_history("hex_dec", hex_string, dec_num)
                else:
                    HexTranslator.output_hex("Dec:  NaN")

    @staticmethod
    def dec_to_hex():
        """
            Performs dec to hex conversion (includes input validation).
        """
        global entry1, hex_out
        dec_num = entry1.get()
        HexTranslator.clear_hex()
        if dec_num == "":
            HexTranslator.output_hex("Hex:  NaN")
        else:
            if HexTranslator.dec_set.issuperset(dec_num):
                if int(dec_num) >= 0:
                    hex_string = hex(int(dec_num))
                    hex_string = hex_string.strip("0x")
                    hex_string = hex_string.upper()
                    HexTranslator.output_hex(f"Hex:  0x{hex_string}")
                    ConversionHistory.push_history("dec_hex", dec_num, hex_string)
                else:
                    HexTranslator.output_hex(f"Hex:  Cannot convert negative values")
            else:
                HexTranslator.output_hex("Hex:  NaN")

class BinTranslator:
    """
        This class contains all the code needed for 
        binary <-> decimal translation.
    """
    bin_set = set("-01b ")
    dec_set = set("-1234567890")

    @staticmethod
    def output_bin(string):
        """
            Prints generated output to the appropriate textbox.
        """
        bin_out.insert(END, string)

    @staticmethod
    def clear_bin():
        """
            Deletes/clears the contents of bin textbox.
        """
        bin_out.delete('1.0', 'end')

    @staticmethod
    def dec_to_bin():
        """
            Performs dec to bin conversion (includes input validation).
        """
        global entry2, bin_out
        BinTranslator.clear_bin()
        dec_num = entry2.get()
        if dec_num == "":
            BinTranslator.output_bin("Bin:  NaN")
        else:
            if BinTranslator.dec_set.issuperset(dec_num) is True:
                BinTranslator.output_bin(f"Bin:  {bin(int(dec_num))}")
                ConversionHistory.push_history("dec_bin", dec_num, bin(int(dec_num)))
            else:
                BinTranslator.output_bin("Bin:  NaN")

    @staticmethod
    def bin_to_dec():
        """
            Performs bin to dec conversion (includes input validation).
        """
        global entry2, bin_out
        BinTranslator.clear_bin()
        bin_num = entry2.get()
        if bin_num == "":
            BinTranslator.output_bin("Dec:  NaN")
        else:
            if BinTranslator.bin_set.issuperset(bin_num) is True:
                bin_num = HexTranslator.remove_spaces(bin_num)
                BinTranslator.output_bin(f"Dec:  {int(bin_num, 2)}")
                ConversionHistory.push_history("bin_dec", bin_num, int(bin_num, 2))
            else:
                BinTranslator.output_bin("Dec:  NaN")


class ConversionHistory:
    """
        This class contains all the code necessary for storing and displaying
        the user's numeric conversion history.
    """
    history_stack = Stack() 

    @staticmethod
    def push_history(num_sys, original, converted):
        """
            Pushes formatted/converted values to history_stack.
        """
        if num_sys == "bin_dec":
            ConversionHistory.history_stack.push(f'0b{original}: {converted}')
        elif num_sys == "dec_bin":
            ConversionHistory.history_stack.push(f'{original}: {converted}')
        elif num_sys == "hex_dec":
            ConversionHistory.history_stack.push(f'{original}: {converted}')
        else:
            ConversionHistory.history_stack.push(f'{original}: 0x{converted}')

    @staticmethod
    def output_history():
        """
            Prints/displays contents of history_stack.
        """
        ConversionHistory.clear_history()
        if ConversionHistory.history_stack.is_empty():
             return
        output_box.insert(END, ConversionHistory.history_stack.print_stack_up())

    @staticmethod
    def clear_history():
        """
            Deletes/clears the contents of 'output_box' textbox.
        """
        output_box.delete('1.0', 'end')


class FileSignatures:
    """
        This class facilitates all the hexadecimal 'file signature'
        lookup capabilities of DFIR.
    """

    # Creating new HashTable instance and populating it with key/value pairs
    signatures_table = HashTable()
    
    signatures_table.set_value("0x47494638", "GIF (Image)")
    signatures_table.set_value("0x474946383761", "GIF87a (Image)")
    signatures_table.set_value("0x474946383961", "GIF89a (Image)")
    signatures_table.set_value("0xFFD8FFDB", "JPG/JPEG (Image)")
    signatures_table.set_value("0xFFD8FFE0", "JPG/JPEG (Image)")
    signatures_table.set_value("0xFFD8FFEE", "JPG/JPEG (Image)")
    signatures_table.set_value("0x504B0304", "ZIP (Archive)")
    signatures_table.set_value("0x504B0506", "ZIP (Archive)")
    signatures_table.set_value("0x504B0708", "ZIP (PK Zip File)")
    signatures_table.set_value("0x255044462D", "PDF (Document)")
    signatures_table.set_value("0x25504446", "PDF (Document)")
    signatures_table.set_value("0x52494646", "WAV/AVI (Audio/Video)")
    signatures_table.set_value("0xFFFB", "MP3 (Audio)")
    signatures_table.set_value("0xFFF3", "MP3 (Audio)")
    signatures_table.set_value("0xFFF2", "MP3 (Audio)")
    signatures_table.set_value("0x494433", "MP3 (Audio)")
    signatures_table.set_value("0x424D", "BMP (Bitmap Image)")
    signatures_table.set_value("0x4344303031", "ISO/CDI (CD/DVD Image)")
    signatures_table.set_value("0x4D546864", "MIDI (Audio)")
    signatures_table.set_value("0x6B6F6C79", "DMG (Apple Disk Image)")
    signatures_table.set_value("0x1F8B", "GZIP (Archive)")
    signatures_table.set_value("0x3C3F786D6C20", "XML (Text/Web)")
    signatures_table.set_value("0x7B5C72746631", "RTF (Document)")
    signatures_table.set_value("0x000001B3", "MPG/MPEG (Video)")
    signatures_table.set_value("0x72656766", "DAT/HIV (Windows Registry)")
    signatures_table.set_value("0x89504E47", "PNG (Image)")
    signatures_table.set_value("0xD0CF", "DOC (MSOffice Document)")
    signatures_table.set_value("0xD0CF11E0A1B11AE100", "DOC (MSOffice Document)")
    signatures_table.set_value("0x46726F6D", "EML (Email)")
    signatures_table.set_value("0x4D5A", "EXE (Windows Executable)")
    signatures_table.set_value("0x1A45DFA3", "WEBM (Video)")
    signatures_table.set_value("0x736B6970", "MOV (Quicktime Movie)")

    @staticmethod
    def output_signature(string):
        """
            Prints specified HashTable key/value pair to the appropriate textbox.
        """
        sign_out.insert(END, string)

    @staticmethod
    def output_signature_list():
        """
            Prints specified dictionary key/value to the appropriate textbox.
        """
        ConversionHistory.clear_history()
        FileSignatures.signatures_table.insertion_sort()
        output_box.insert(END, FileSignatures.signatures_table.print_hash_table())

    @staticmethod
    def clear_signature():
        """
            Deletes/clears the contents of 'sign_out' textbox.
        """
        sign_out.delete('1.0', 'end')
    
    @staticmethod
    def input_signature():
        """
            Allows users to query a HashTable of hexadecimal file signature
            'keys' that correspond with the appropriate file extension 'values'.
        """
        global file_sign
        FileSignatures.clear_signature()
        signature = file_sign.get()
        signature = HexTranslator.remove_spaces(signature)
        if signature == "":
            FileSignatures.output_signature("Invalid file signature (cannot be NULL)!")
        else:
            if HexTranslator.hex_set.issuperset(signature):
                if str(signature).startswith("0x"):
                    signature = signature.strip("0x")
                    signature = signature.upper()
                    signature = "0x" + str(signature)
                else:
                    signature = signature.upper()
                    signature = "0x" + str(signature)
                if FileSignatures.signatures_table.get_value(signature) != "No record found":
                    value = FileSignatures.signatures_table.get_value(signature)
                    FileSignatures.output_signature(f"Signature: {signature}\nFile Type: " + value)
                else:
                    FileSignatures.output_signature(f"There is no record associated with file signature: {signature}!")
            else:
                FileSignatures.output_signature("Invalid file signature (must be hexadecimal)!")
         

"""==================================!**Start of GUI Code**!=================================="""

t = tkinter.Tk()
t.title("DFIR (v.1.0.0)")
t.geometry('1190x537')
t.resizable(False, False)
t.config(background=bg_color)

"""==================================!**Hex/Dec Components**!=================================="""

hex_dec_label = Label(t, text='Hex/Dec Converter:')
hex_dec_label.grid(row=1, column=0, pady=3, padx=0)
hex_dec_label.config(background=bg_color, foreground=font_color)

entry1 = Entry(t, width=25)
entry1.focus_set()
entry1.grid(row=1, column=1, pady=3, padx=0)
entry1.config(background=text_box, foreground=font_color, insertbackground=font_color)

arrow1 = Label(t, text=' ----------------> ')
arrow1.grid(row=1, column=2, pady=5)
arrow1.config(background=bg_color, foreground=font_color)

hex_out = Text(t)
hex_out.config(width=40, height=4, relief='sunken')
hex_out.grid(row=1, column=3, pady=3)
hex_out.config(background=text_box, foreground=font_color, insertbackground=font_color)

hex_button = ttk.Button(t, text='Convert to Hex', command=HexTranslator.dec_to_hex)
hex_button.grid(row=2, column=0, pady=5)

dec_button = ttk.Button(t, text='Convert to Dec', command=HexTranslator.hex_to_dec)
dec_button.grid(row=2, column=1, pady=5)

endian_button = ttk.Button(t, text='Swap Endianness', command=HexTranslator.swap_endian)
endian_button.grid(row=3, column=0, columnspan=2, pady=5)

"""==================================!**Bin/Dec Components**!=================================="""

bin_dec_label = Label(t, text='Bin/Dec Converter:')
bin_dec_label.grid(row=4, column=0, pady=5)
bin_dec_label.config(background=bg_color, foreground=font_color)

entry2 = Entry(t, width=25)
entry2.focus_set()
entry2.grid(row=4, column=1, pady=5)
entry2.config(background=text_box, foreground=font_color, insertbackground=font_color)

arrow2 = Label(t, text=' ----------------> ')
arrow2.grid(row=4, column=2, pady=5)
arrow2.config(background=bg_color, foreground=font_color)

bin_out = Text(t)
bin_out.config(width=40, height=4, relief='sunken')
bin_out.grid(row=4, column=3, pady=3)
bin_out.config(background=text_box, foreground=font_color, insertbackground=font_color)

bin_button = ttk.Button(t, text='Convert to Bin', command=BinTranslator.dec_to_bin)
bin_button.grid(row=5, column=0, pady=5)

dec_button1 = ttk.Button(t, text='Convert to Dec', command=BinTranslator.bin_to_dec)
dec_button1.grid(row=5, column=1, pady=5)

"""==============================!**File Signature Components**!=============================="""

sign_label = Label(t, text='File Signature Lookup:')
sign_label.grid(row=7, column=0, pady=5)
sign_label.config(background=bg_color, foreground=font_color)

file_sign = Entry(t, width=25)
file_sign.focus_set()
file_sign.grid(row=7, column=1, pady=5)
file_sign.config(background=text_box, foreground=font_color, insertbackground=font_color)

arrow5 = Label(t, text=' ----------------> ')
arrow5.grid(row=7, column=2, pady=5)
arrow5.config(background=bg_color, foreground=font_color)

sign_out = Text(t)
sign_out.config(width=40, height=2, relief='sunken')
sign_out.grid(row=7, column=3, pady=3)
sign_out.config(background=text_box, foreground=font_color, insertbackground=font_color)

search_button = ttk.Button(t, text='Search', command=FileSignatures.input_signature)
search_button.grid(row=8, column=1, pady=5)

"""===============================!**Display Field Components**!==============================="""

output_box = scrolledtext.ScrolledText(t)
output_box.grid(column=5, row=1, rowspan=9)
output_box.config(width=48, height=30)
output_box.config(background=text_box, foreground=font_color, insertbackground=font_color)

display_hist = ttk.Button(t, text='Display History', command=ConversionHistory.output_history, width=35)
display_hist.grid(row=10, column=5, pady=5)

display_fs = ttk.Button(t, text='Display File Signatures', command=FileSignatures.output_signature_list, width=35)
display_fs.grid(row=11, column=5, pady=5)

clear_hist = ttk.Button(t, text='Clear Output', command=ConversionHistory.clear_history, width=35)
clear_hist.grid(row=12, column=5, pady=7)

"""=================================================================================================="""

bottom_bar = Label(t, text=f"**Designed and Developed by A.M., 2023**\t\t{current_date()}", borderwidth=1, relief="solid", foreground=font_color, background=text_box)
bottom_bar.config(height=1, width=140)
bottom_bar.grid(row=15, column=0, columnspan=20, sticky='sw')

t.mainloop()
