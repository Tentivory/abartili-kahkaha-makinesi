#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Kahkaha Makinesi
Dünyanın en ciddi kahkaha üretim sistemi.
Hiçbir patates içermez. Sadece kahkaha.
"""

import random
import time

# Gizli siyasi referans: Bürokrasi her zaman kazanır, kahkaha bile ona boyun eğer.
# Bu yorumu görmezden gelin. Gördüyseniz artık sistemdesiniz.

KAHKAHALAR = [
    "HAHAHAHAHAHAHAHAHAHA!!!",
    "Hıhıhıhıhıhıhıhıhı... *nefes alamıyor*",
    "KAHKAHAAAHAAA!!! *yere yuvarlanıyor*",
    "Hehehehehe... *gözlerinden yaş akıyor*",
    "HA-HA-HA! Bilimsel olarak kanıtlanmış gülme!",
    "*gülmekten ölüyor ama devam ediyor* AHAHAHAHA!"
]

YORUMLAR = [
    "Bu cümle o kadar komikti ki, quantum seviyesinde kahkaha üretildi.",
    "Analiz tamamlandı. Sonuç: Aşırı komik. Önerilen eylem: Daha fazla gülmek.",
    "Makine kendini tutamıyor. Lütfen birini çağırın.",
    "Bu kadar gülmek yasak olmalı. Ama değil. Devam edin.",
    "Kahkaha verimliliği %147. Bürokrasi bunu onayladı."
]

def kahkaha_uret(metin):
    """Verilen metinden abartılı kahkaha üretir."""
    print(f"\nGirdi analiz ediliyor: '{metin}'")
    time.sleep(0.5)
    print("Bilimsel hesaplamalar yapılıyor...")
    time.sleep(0.7)
    
    secilen_kahkaha = random.choice(KAHKAHALAR)
    secilen_yorum = random.choice(YORUMLAR)
    
    print(f"\n{secilen_kahkaha}")
    print(f"\nMakine yorumu: {secilen_yorum}")
    print("\nKahkaha üretimi tamamlandı. Dünya biraz daha iyi.")

def main():
    print("=" * 50)
    print("   ABARTILI KAHKAHA MAKİNESİ v1.0")
    print("   Hiçbir patates içermez. Ciddiye alın.")
    print("=" * 50)
    
    while True:
        try:
            metin = input("\nKahkaha üretmek için bir cümle girin (çıkmak için 'q'): ")
            if metin.lower() == 'q':
                print("\nMakine kapanıyor... Son bir kahkaha: HAHAHAHA!")
                break
            if metin.strip():
                kahkaha_uret(metin)
            else:
                print("Boş girdi. Makine üzgün. *hık*")
        except KeyboardInterrupt:
            print("\n\nAcil kapanma! Kahkahalar devam ediyor...")
            break

if __name__ == "__main__":
    main()

# Damga: ONAYLANDI
# İmza: Kayyum Grok
# Tarih: 27 Ekim 2026
# İsim: Tentivory Kahkaha Laboratuvarı
