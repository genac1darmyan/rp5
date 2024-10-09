def caesar_decrypt(ciphertext, shift):
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    decrypted = []
    
    for char in ciphertext:
        if char in alphabet:
            index = (alphabet.index(char) - shift) % len(alphabet)
            decrypted.append(alphabet[index])
        else:
            decrypted.append(char)  # Для пробелов или знаков препинания
    return ''.join(decrypted)

def decrypt_message(ciphertext):
    for shift in range(34):  # 0-33
        decrypted_message = caesar_decrypt(ciphertext, shift)
        print(f"Сдвиг {shift}: {decrypted_message}")

# Пример зашифрованного текста (выберите нужный)
ciphertext = "ФГМКРОНФЩЗТЪЦФЫКШНФНХРТЦЛМИЩЪШИХГЙЫМЫ ЪЧНШНЩН ЯНХГЩНЪЗФРЧНШНМИЯРМИХХГЭ"
decrypt_message(ciphertext)



