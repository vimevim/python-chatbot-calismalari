import string
import random
inputOutputDict = {
    "merhaba" :["Merhaba.","Selam","Merhaba hoşgeldiniz.","Merhabalar","Selamlar"],
    "hoş buldum" : "",#tepkisiz
    "hoş bulduk" : "",
    "nasılsın" : "İyiyim efendim, siz nasılsınız?",
    "iyiyim" : "Bunu duyduğuma sevindim.",
    "2 artı 2 kaç eder" :"4 eder efendim",
    "ankarada hava durumu ne" : "Soğuk, brrrrr.",
    "adın ne" : "Benim adım Ayelar",
    "ismin ne" :"adın ne",#aynı soruların cevaplarını eşleştir
    "senin adın ne" : "adın ne"
}
def ciktiAl(girdi):
    # kullanıcı bir şey girmezse pass geçiyoruz
    if girdi =="":
        pass
    # kullanıcının girdisi sözlükte yoksa "ne dediğini anlamadım." cevabını veriyoruz
    elif girdi not in inputOutputDict:
        print("Ne dediğinizi anlamadım.")
    # eğer girdinin çoklu cevabı varsa random üretip random indexini çağırıyoruz
    elif isinstance(inputOutputDict[girdi], list) == True:
        rand = random.randint(0, len(inputOutputDict[girdi]) - 1)
        # girdinin rastgele indeksini çağırıyoruz
        print(inputOutputDict[girdi][rand])
    # kullanıcı girdisinin karşılığı varsa karşılık dictionary içerisinde var mı kontrol ediyoruz
    elif str(inputOutputDict[girdi]) in inputOutputDict:#list değeri str ile kıyaslanamadığı için str() dönüşümü uygulandı
        print(inputOutputDict[inputOutputDict[girdi]])
    # kullanıcı girdisinin dictionary içerisinde var mı kontrol ediyoruz
    elif girdi in inputOutputDict:
        print(inputOutputDict[girdi])#girdi sözlükte varsa değerini veriyoruz
# diyalogu sonsuz döngüye sokuyoruz
while(True):
    # kullanıcıdan girdi alıyoruz
    userInput = input("User: ")
    # kullanıcı girdisini küçük harfe çeviriyoruz
    userInput=userInput.lower()
    # kullanıcı girdisinde ki noktalama işaretlerini yok ediyoruz
    userInput = "".join([c for c in userInput if c in string.digits + string.ascii_letters + "ÖÜÇŞĞöüçşıİğ "])
    ciktiAl(userInput)