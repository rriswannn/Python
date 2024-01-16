import random
#import dulu module random untuk mensimulasikan lemparan dadu


#Definisikan fungsi "roll" nantinya untuk menghasilkan bilangan bulat acak dari 1 - 6
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

#Mendapatkan jumlah pemain, nantinya pengguna bakal masukin 2-4 pemain
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit(): #.isdigit disini digunnakan untuk memeriksa apakah string terdiri dari numerik, kalau ya maka dijalankan.
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

#inisialisasi variabel dan loop permainan (max_score nanti menentukan skor max yang diperlukan untuk menang)
max_score = 50
player_scores = [0 for _ in range(players)] #misal nanti ada 3 pemain maka scorenya = [0, 0, 0]

while max(player_scores) < max_score: #kalau score max pemain kurang dari max score yang ditetapkan, maka game berlanjut.
    for player_idx in range(players): #ini loop berjalannya pemain
        print("\nPlayer number", player_idx + 1, "turn has just started!") #mencetak baris skor
        print("Your total score is:", player_scores[player_idx], "\n") #mencetak baris skor
        current_score = 0 #inisialisasi skor sementara

#giliran setiap pemain (apakah mereka mau melempar dadu, kalau ya nanti fungsi roll akan dipanggil)
        while True: #loop tak terbatas
            should_roll = input("Would you like to roll (y)? ") #pertanyaan buat lempar dadu
            if should_roll.lower() != "y": #mengecek input pemain, kalau ga sama bakal distop
                break

            value = roll()#melempar dadu
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:#jika nilai dadu bukan 1, maka akan ditambahkan ke skor sementara pemain
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score) #cetak skor sementara

        player_scores[player_idx] += current_score #perbarui skor total pemain
        print("Your total score is:", player_scores[player_idx]) #cetak skor total pemain

#pencacatan score dan penentuan pemenang 
max_score = max(player_scores) #mendapatkan skor tertingg
winning_idx = player_scores.index(max_score) #menentukan pemenang, 'index() memberikan informasi pemain mana yang skonya paling tinggi
print("Player number", winning_idx + 1, #mencetak informasi pemenang
      "is the winner with a score of:", max_score)


#Ini merupakan latihan python sederhana ya!