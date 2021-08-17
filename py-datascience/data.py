# import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

siswa = np.array([18, 20, 16, 15, 18, 25])
kelas = np.array([ 1,  2,  3,  4,  5,  6])

def read():
	for i in range(len(kelas)):
		print(" Kelas %d - Jumlah Siswa = %d" % (kelas[i], siswa[i]))

def saveToPict(filename):
	plt.plot(kelas, siswa, label='linear', color='red')

	plt.title('Data Jumlah Siswa')
	plt.ylabel('Jumlah Siswa')
	plt.xlabel('Kelas')
	plt.legend()

	plt.savefig(filename)

user = input('ingin save kt graphic?? [y/n]')

if user == 'y' :
	filename = input('Masukkan nama file : ')
	saveToPict(filename)
else :
	print('OK BYE!!')



