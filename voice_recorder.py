import queue
import tkinter as tk
import sounddevice as sd
from tkinter import *
import soundfile as sfl
import threading
from tkinter import messagebox

#Threading allows parallel execution of various processes, by this, we can keep other buttons active even if a funtion is acting on the click of other button

def threading_rec(x):
   if x == 1:                                                               #starts recording
       #if recording is selected, thread activated
       t1=threading.Thread(target= record_audio)
       t1.start()
   elif x == 2:                                                             #stops recording
       #To stop, set false
       global recording
       recording = False
       messagebox.showinfo(message="Recording finished")
   elif x == 3:                                                             #plays the recording
       #To play a recording, it must exist.
       if file_exists:
           #Read the recording if it exists and play it
           data, fs = sd.read("trial.wav", dtype='float64')
           sd.play(data,fs)
           sd.wait()
       else:
           #Display and error if none is found
           messagebox.showerror(message="Record something to play")


# We have three main functions: threading, callback, record
# play is used to record data into queue

def play(indata, frames, time, status):     
   q.put(indata.copy())
   

def record_audio():
   #Declare global variables   
   global recording
   #Set to True to record
   recording= True  
   global file_exists
   #Create a file to save the audio
   messagebox.showinfo(message="Speak into your microphone please. :)")
   with sfl.SoundFile("trial.wav", mode='w', samplerate=45000,
                       channels=2) as myrecording:
   #Create an input stream to record audio without a preset time
           with sd.InputStream(samplerate=45000, channels=2, callback= play):
               while recording == True:
                   #Set the variable to True to allow playing the audio later
                   myrecording_exist =True
                   #write into file
                   myrecording.write(q.get())

#GUI for VOICE RECORDER

voice_rec = tk.Tk()

voice_rec.title("VOICE RECORDER")
voice_rec_frame = tk.Frame(master= voice_rec, bg= 'Black', padx =5)
q= queue.Queue()

recording = False
file_exists = False

title= Label(voice_rec, text= voice_rec, bg= "blue").grid(row= 0, column = 0, columnspan = 3)
record_btn =Button(voice_rec, text= "Record Audio", command= lambda a=1:threading_rec(a))
stop_btn = Button(voice_rec, text = "Stop", command= lambda a=2:threading_rec(a))
play_btn= Button(voice_rec, text= "Play", command= lambda a=3:threading_rec(a))
record_btn.grid(row=1,column=1)
stop_btn.grid(row=1,column=0)
play_btn.grid(row=1,column=2)
voice_rec.mainloop()


