#!/bin/bash
NAMA_FILE="users.txt"

if [ ! -f "$NAMA_FILE" ]; then
    echo "Error: File $NAMA_FILE tidak ditemukan!"
    exit 1
fi

while IFS= read -r user || [ -n "$user" ]; do
    user=$(echo "$user" | xargs)
    [ -z "$user" ] && continue

    # Membuat user baru
    sudo useradd -m -s /bin/bash "$user" 2>/dev/null
    
    if [ $? -eq 0 ]; then
        PASSWORD="${user}@123"
        echo "${user}:${PASSWORD}" | sudo chpasswd
        echo "Sukses: User '$user' berhasil dibuat dengan password '$PASSWORD'"
    else
        echo "Info: User '$user' sudah ada di sistem."
    fi
done < "$NAMA_FILE"
echo "--------------------------------------------------"
