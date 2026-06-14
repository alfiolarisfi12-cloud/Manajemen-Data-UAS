#!/bin/bash

# Mengambil persentase ruang hdd yang LUANG/SISA pada disk utama (/)
# df / mengembalikan baris penggunaan. Kita kalkulasi 100 - %terpakai
TERPAKAI=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
SISA=$((100 - TERPAKAI))

# Menampilkan report notifikasi sesuai format soal
echo "========================================="
echo "space hdd anda tinggal ${SISA}%"
echo "========================================="
